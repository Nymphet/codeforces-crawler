# -*- coding: utf-8 -*-

import scrapy

from CodeforcesSpider.items import CodeforcesSolutionItem

class CodeforcesSolutionSpider(scrapy.Spider):
    name = "CodeforcesSolution"
    allowed_domains = ["codeforces.com"]
    start_urls = ["http://codeforces.com/problemset/"]

    def parse(self, response):
        for solution_href in response.selector.xpath('//a[@title="Participants solved the problem"]/@href'):
            solution_url = response.urljoin(
                solution_href.extract() + '?order=BY_CONSUMED_TIME_ASC')
            yield scrapy.Request(solution_url, callback=self.parse_problem_solution_list_page)

        if response.selector.xpath('//span[@class="inactive"]/text()').extract():
            if response.selector.xpath('//span[@class="inactive"]/text()')[0].extract() != u'\u2192':
                next_page_href = response.selector.xpath(
                    '//div[@class="pagination"]/ul/li/a[@class="arrow"]/@href')[0]
                next_page_url = response.urljoin(next_page_href.extract())
                yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            next_page_href = response.selector.xpath(
                '//div[@class="pagination"]/ul/li/a[@class="arrow"]/@href')[1]
            next_page_url = response.urljoin(next_page_href.extract())
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_problem_solution_list_page(self, response):
        solution_id_list = response.xpath('//tr/@data-submission-id').extract()
        for solution in solution_id_list:
            yield scrapy.FormRequest.from_response(response, url='http://codeforces.com/data/submitSource',
                                     formdata={'submissionId': solution},
                                     callback=self.parse_solution)

    def parse_solution(self, response):
        item = CodeforcesSolutionItem()
        item['s_json'] = response.body
        yield item
