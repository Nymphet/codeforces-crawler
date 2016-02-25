# -*- coding: utf-8 -*-

import scrapy
import json
import re

from CodeforcesSpider.items import CodeforcesTestDataItem


class CodeforcesSolutionSpider(scrapy.Spider):
    name = "CodeforcesTestData"
    allowed_domains = ["codeforces.com"]
    start_urls = ["http://codeforces.com/problemset/"]

    p_id = re.compile(r'''/(\d+)/''')
    p_index = re.compile(r'''problem/(.+)\?''')

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
        first_solution = response.xpath('//tr/@data-submission-id')[0].extract()
        yield scrapy.FormRequest.from_response(response, url='http://codeforces.com/data/submitSource',
                                               formdata={
                                                   'submissionId': first_solution},
                                               meta={'p_id': self.p_id.search(response.url).group(
                                                   1), 'p_index': self.p_index.search(response.url).group(1)},
                                               callback=self.parse_solution)

    def parse_solution(self, response):

        json_response = json.loads(response.body)

        item = CodeforcesTestDataItem()

        item['d_id'] = response.meta['p_id']
        item['d_index'] = response.meta['p_index']
        item['d_json'] = json_response

        yield item
