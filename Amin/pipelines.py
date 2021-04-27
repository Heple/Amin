# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import redis
from redis import Redis

from Amin.items import AminItem, CommentsItem

red = Redis(decode_responses=True)


class AminPipeline:
    def process_item(self, item, spider):
        if isinstance(item, AminItem):
            self.adim_item(item,spider)
        elif isinstance(item,CommentsItem):
            self.com_item(item, spider)
            with open('b.txt', 'a', encoding='utf-8') as f:
                f.write(str(item['user']) + '\n')
                f.close()
        red.save()
        return item

    def com_item(self, item, spider):
        for i in range(0, len(item['user'])):
            red.lpush('user', item['user'][i])
            red.lpush('content', item['content'][i])

    def adim_item(self,item,spider):
        for i in range(0, len(item['title'])):
            red.lpush('title', item['title'][i])
            red.lpush('price', item['price'][i])
            red.lpush('img', item['img'][i])
            red.lpush('pti', item['pti'][i])