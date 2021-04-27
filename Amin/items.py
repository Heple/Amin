# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AminItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    price=scrapy.Field()
    img=scrapy.Field()
    pti=scrapy.Field()
    pass

class CommentsItem(scrapy.Item):
    user=scrapy.Field()
    content=scrapy.Field()
    pass