# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CodeforcesProblemItem(scrapy.Item):

    p_id                    = scrapy.Field()
    p_index                 = scrapy.Field()
    p_title                 = scrapy.Field()
    p_time_limit            = scrapy.Field()
    p_memory_limit          = scrapy.Field()
    p_input_file            = scrapy.Field()
    p_output_file           = scrapy.Field()
    p_statement             = scrapy.Field()
    p_input_specification   = scrapy.Field()
    p_output_specification  = scrapy.Field()
    p_sample_tests          = scrapy.Field()
    p_note                  = scrapy.Field()


class CodeforcesTutorialItem(scrapy.Item):

    t_contest_ids           = scrapy.Field()
    t_topic_title           = scrapy.Field()
    t_url                   = scrapy.Field()
    t_content               = scrapy.Field()
    t_comments              = scrapy.Field()


class CodeforcesSolutionItem(scrapy.Item):

    s_json                  = scrapy.Field()
