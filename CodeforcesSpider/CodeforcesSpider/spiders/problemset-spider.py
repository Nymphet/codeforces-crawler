# -*- coding: utf-8 -*-

import scrapy

from CodeforcesSpider.items import CodeforcesProblemItem

class CodeforcesProblemSpider(scrapy.Spider):
    name = "CodeforcesProblem"
    allowed_domains = ["codeforces.com"]
    start_urls = ["http://codeforces.com/problemset/"]


    def parse(self, response):
        for problem_href in response.selector.xpath('//td[@class="id"]/a/@href'):
            problem_url = response.urljoin(problem_href.extract())
            yield scrapy.Request(problem_url, callback=self.parse_problem_contents)

        if response.selector.xpath('//span[@class="inactive"]/text()').extract():
            if response.selector.xpath('//span[@class="inactive"]/text()')[0].extract() != u'\u2192':
                next_page_href = response.selector.xpath('//div[@class="pagination"]/ul/li/a[@class="arrow"]/@href')[0]
                next_page_url  = response.urljoin(next_page_href.extract())
                yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            next_page_href = response.selector.xpath('//div[@class="pagination"]/ul/li/a[@class="arrow"]/@href')[1]
            next_page_url  = response.urljoin(next_page_href.extract())
            yield scrapy.Request(next_page_url, callback=self.parse)


    def parse_problem_contents(self, response):
        item = CodeforcesProblemItem()
        item['p_id']                    = response.selector.xpath('//title').re('- (\d*)[a-zA-Z]*\d* -')[0]
        item['p_index']                 = response.selector.xpath('//div/@problemindex').extract()[0]
        item['p_title']                 = response.selector.xpath('//div[@class="header"]/div[@class="title"]/text()')[0].extract()
        item['p_time_limit']            = response.selector.xpath('//div[@class="header"]/div[@class="time-limit"]/text()')[0].extract()
        item['p_memory_limit']          = response.selector.xpath('//div[@class="header"]/div[@class="memory-limit"]/text()')[0].extract()
        item['p_input_file']            = response.selector.xpath('//div[@class="header"]/div[@class="input-file"]/text()')[0].extract()
        item['p_output_file']           = response.selector.xpath('//div[@class="header"]/div[@class="output-file"]/text()')[0].extract()
        item['p_statement']             = response.selector.xpath('//div[@class="problem-statement"]/div')[1].extract()
        item['p_input_specification']   = response.selector.xpath('//div[@class="input-specification"]')[0].extract()
        item['p_output_specification']  = response.selector.xpath('//div[@class="output-specification"]')[0].extract()
        item['p_sample_tests']          = response.selector.xpath('//div[@class="sample-tests"]/div[@class="sample-test"]/div').extract()
        item['p_note']                  = response.selector.xpath('//div[@class="note"]/p').extract()
        yield item
