import scrapy
from redis import Redis
from scrapy import Selector
from scrapy.http import Request
from scrapy.spiders.crawl import Rule
from scrapy.linkextractors import LinkExtractor
from Amin.items import CommentsItem

red = Redis(decode_responses=True)
class AdimSpider(scrapy.Spider):
    name = 'com'
    allowed_domains = ['amazon.cn']
    start_urls = ['https://www.amazon.cn/product-reviews']

    def parse(self, response, **kwargs):
        for j in red.lrange('pti', 0, (red.llen('pti'))):
            for i in range(1, 10):
                start_urls = 'https://www.amazon.cn/product-reviews/' + j + '/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(i)
                yield Request(url=start_urls,callback=self.com_parse)

    def com_parse(self,response):
        com = CommentsItem()
        for i in range(2, 11):
            com['user'] = response.xpath(f'/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div[{i}]/div/div/div[1]/a/div[2]/span/text()').extract()
            com['content']=response.xpath(f'/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div[{i}]/div/div/div[4]/span/span/text()').extract()
            print(com['content'])
            yield com