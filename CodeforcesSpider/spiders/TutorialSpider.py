# -*- coding: utf-8 -*-

import scrapy
import logging

from CodeforcesSpider.items import CodeforcesTutorialItem


class CodeforcesTutorialSpider(scrapy.Spider):
    name = "CodeforcesTutorial"
    allowed_domains = ["codeforces.com"]
    start_urls = ["http://codeforces.com/contests/"]


    def parse(self, response):
        for contest_id in response.selector.xpath('//div[@class="contests-table"]/div[@class="datatable"]/div/table/tr/@data-contestid').extract():
            contest_url = "http://codeforces.com/contests/" + contest_id
            yield scrapy.Request(contest_url, callback=self.parse_tutorial_url)

        if response.selector.xpath('//span[@class="inactive"]/text()').extract():
            if response.selector.xpath('//span[@class="inactive"]/text()')[0].extract() != u'\u2192':
                next_page_href = response.selector.xpath('//div[@class="pagination"]/ul/li/a[@class="arrow"]/@href')[0]
                next_page_url  = response.urljoin(next_page_href.extract())
                yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            next_page_href = response.selector.xpath('//div[@class="pagination"]/ul/li/a[@class="arrow"]/@href')[1]
            next_page_url  = response.urljoin(next_page_href.extract())
            yield scrapy.Request(next_page_url, callback=self.parse)


    def parse_tutorial_url(self, response):
        if response.selector.xpath('//a[text()="Tutorial"]/@href'):
            tutorial_href = response.selector.xpath('//a[text()="Tutorial"]/@href')[0]
            tutorial_url = response.urljoin(tutorial_href.extract())
            yield scrapy.Request(tutorial_url, callback=self.parse_tutorial_contents)
        elif len(response.selector.xpath('//a[contains(., "Enter")]/@href')) > 1:
            contest_href = response.selector.xpath('//a[contains(., "Enter")]/@href')[1]
            contest_url = response.urljoin(contest_href.extract())
            yield scrapy.Request(contest_url, callback=self.parse_tutorial_url)
        else:
            logging.error("No tutorial find for %s." % (response.url))


    def parse_tutorial_contents(self, response):
        item = CodeforcesTutorialItem()
        item['t_contest_ids']   = response.selector.xpath('//div[@class="topic"]').re('Tutorial of .*/contest/(.*)" class')
        item['t_topic_title']   = response.selector.xpath('string(//div[@class="topic"]/div[@class="title"]/a)')[0].extract()
        item['t_url']           = response.urljoin(response.selector.xpath('//div[@class="topic"]/div[@class="title"]/a/@href')[0].extract())
        item['t_content']       = response.selector.xpath('//div[@class="topic"]/div[@class="content"]')[0].extract()
        item['t_comments']      = response.selector.xpath('//div[@class="topic"]/div[@class="comments"]/div[@class="comment"]').extract()
        yield item
