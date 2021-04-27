import scrapy

from Amin.items import AminItem


class AdimSpider(scrapy.Spider):
    name = 'adim'
    allowed_domains = ['amazon.cn']
    print('输入你需要的商品信息:')
    keys=input()
    start_urls = ['https://www.amazon.cn/s?k='+str(keys)+'&page=%s&__mk_zh_CN=亚马逊网站&qid=1618883480&ref=sr_pg_1' % i for i in range(1,10)]

    def parse(self, response, **kwargs):
        admin = AminItem()
        for i in range(2,49):
            basexpath=f'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/'
            xpathpath=self.xpathselect(response,i,basexpath)
            adimg=response.xpath(xpathpath).extract()
            if adimg==[]:xpathpath=self.Other(i,response,basexpath)
            adimg = response.xpath(xpathpath).extract()
            admin['title'] = self.Noe(response.xpath(f'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[2]/h2/a/span/text()').extract())
            admin['price'] =self.Noe(adimg)
            admin['img']=self.Noe(response.xpath(f'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/span/a/div/img/@src').extract())
            admin['pti']=self.Noe(response.xpath(f'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/@data-asin').extract())
            yield admin

    def xpathselect(self,res,i,basexpath):
        xj = res.xpath(f'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[3]/div/span[1]/span/a/i[1]/span/text()')
        if xj == []:
            basexpath += 'div[3]/'
        else:
            basexpath += 'div[4]/'
        xj=res.xpath(f'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[2]/div')
        if xj==[]:
            basexpath+='div/'
        else:
            basexpath += 'div[2]/'
        xj=res.xpath(f'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[4]/div[3]/span/text()')
        if xj==[]:
            pass
        else:
            basexpath+='div/'
        basexpath+='a/span/span[1]/text()'
        return basexpath

    def Other(self,i,res,basexpath):
        xj = res.xpath(f'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[4]/div[2]/span[1]')
        zj=res.xpath(f'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[{i}]/div/span/div/div/div[3]/div/span[1]/span/a/i[1]/span/text()')
        if zj==[]:
            basexpath += 'div[3]/'
        else:
            basexpath += 'div[4]/'
        if xj==[]:
            basexpath+='div[2]/'
        else:
            basexpath+='div[1]/'
        basexpath += 'a/span/span[1]/text()'
        return basexpath

    def Noe(self,item):
        if item==[]:
            return 'NON'
        else:
            return item