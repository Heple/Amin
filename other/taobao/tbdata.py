import requests
import os
import json
import re
import time
import random
import xl
import pandas as pd
import Proxies
res=requests.Session()
GOODS_EXCEL_PATH=r'C:\Users\Administrator\Desktop\data_cat.xlsx'
COOKIES_FILE_PATH = '../../../../Erp/taobao_cookies.txt'
print(Proxies.proxies)
my_taobao_url = 'http://i.taobao.com/my_taobao.htm'
heawder={
    'referer':'https://s.taobao.com/search',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'

}
with open(COOKIES_FILE_PATH, 'r+', encoding='utf-8') as file:
    cookies_dict = json.load(file)
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    res.cookies = cookies

def load_data(s,q):
    print(res.cookies)
    search_url = f'https://s.taobao.com/search?data-key=s&data-value={s*44}&ajax=false&callback=jsonp744&q={q}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210323&ie=utf8&bcoffset=0&ntoffset=6&p4ppushleft=l,48&s={(s-1)*44}'
    try:
        reust=res.get(url=search_url,headers=heawder,proxies=Proxies.proxies)
        match_re = re.search(r'g_page_config = (.*?)}};', reust.text)
        print(match_re.group(1))
        return match_re.group(1) + '}}'
    except Exception as e:
        print('失败,正在重试')
        lg = xl.Login(res)
        lg.getstpath()
        lg.setcookies()
        with open(COOKIES_FILE_PATH, 'r+', encoding='utf-8') as file:
            cookies_dict = json.load(file)
            cookies = requests.utils.cookiejar_from_dict(cookies_dict)
            res.cookies = cookies
        load_data(s,q)

def _get_goods_info(goods_str):
    goods_json = json.loads(goods_str)
    goods_items = goods_json['mods']['itemlist']['data']['auctions']
    goods_list = []
    for goods_item in goods_items:
        goods = {'title': goods_item['raw_title'],
                 'price': goods_item['view_price'],
                 'location': goods_item['item_loc'],
                 'sales': goods_item['view_sales'],
                 'comment_url': goods_item['comment_url']}
        goods_list.append(goods)
    return goods_list



def _save_excel(goods_list):

    if os.path.exists(GOODS_EXCEL_PATH):
        df = pd.read_excel(GOODS_EXCEL_PATH)
        df = df.append(goods_list)
    else:
        df = pd.DataFrame(goods_list)

    writer = pd.ExcelWriter(GOODS_EXCEL_PATH)
    df.to_excel(excel_writer=writer, columns=['title', 'price', 'location', 'sales', 'comment_url'], index=False,
                encoding='utf-8', sheet_name='Sheet')
    writer.save()
    writer.close()


def patch_spider_goods():
    for i in range(1,10):
        print('第%d页' % (i + 1))
        time.sleep(random.randint(10, 15))
        _save_excel(_get_goods_info(load_data(i,'猫')))
patch_spider_goods()