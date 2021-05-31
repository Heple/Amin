import hashlib
import requests
import json
import time
import os
import re
res = requests.Session()
head = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-type': 'application/x-www-form-urlencoded',
    # 'Host': 'acs.youku.com',
    'Origin': 'https://so.youku.com',
    'referer': 'https://so.youku.com/search_video/q_love_1?searchfrom=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
open('cook.txt','w')
def savecookie():
    if  not os.path.exists('cook.txt'):
        os.startfile('cook.txt')
    with open('cook.txt', 'w+', encoding='utf-8') as file:
        json.dump(res.cookies, file)
        print('保存cookies文件成功！')


def initcookie():
    with open('cook.txt', 'r+', encoding='utf-8') as file:
        cookies_dict = json.load(file)
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        res.cookies = cookies


def fistcookie():
    ul = 'https://so.youku.com/search_video/q_love_1?searchfrom=1'
    baul = 'https://www.youku.com/'
    res.get(url=baul, headers=head)
    ck = requests.utils.dict_from_cookiejar(res.cookies)
    res.cookies = ck
    print(res.cookies)
    savecookie()
    initcookie()
    print(res.cookies)
    co = res.get(url=ul, headers=head)
    import re
    py = re.search('window.__INITIAL_DATA__ =({.*}),', co.text)
    print(py.group(1))
    print(res.cookies)
    ck = requests.utils.dict_from_cookiejar(res.cookies)
    res.cookies = ck
    savecookie()
import random

def save(t, sign, data):
    url = 'https://acs.youku.com/h5/mtop.youku.soku.yksearch/2.0/?jsv=2.5.1&appKey=23774304&t=' + str(t) + '&sign=' + sign + '&api=mtop.youku.soku.yksearch&type=originaljson&v=2.0&ecode=1&dataType=json&jsonpIncPrefix=headerSearch&data=' + data
    res.get(url=url, headers=head)
    ck = requests.utils.dict_from_cookiejar(res.cookies)
    res.cookies = ck
    print(res.cookies)
    savecookie()
    initcookie()
save('t', '', 'data')
def start(page):
    appkey = '23774304'
    t = int(time.time() * 1000)
    data = '{"searchType":1,"keyword":"love%3D1","pg":' + str(page) + ',"pz":20,"site":1,"appCaller":"pc","appScene":"mobile_multi","userTerminal":2,"sdkver":313,"userFrom":1,"noqc":0,"aaid":"8c89eebf790cae2c1d40be03e0fed7c6","ftype":0,"duration":"","categories":"","ob":"","utdId":"Z7fyGAioincCAa8GBuIP+8Cl","userType":"guest","userNumId":0,"searchFrom":"2","sourceFrom":"home"}'
    ck = open('cook.txt', 'r').read()
    print(data)
    c = re.search('_m_h5_tk": "(.*?)_', ck).group(1)
    cks = re.search('_m_h5_tk": "(.*?)",', ck).group(1)
    cksn = re.search('_m_h5_tk_enc": "(.*?)"}', ck).group(1)
    key = c + '&' + str(t) + '&' + appkey + '&' + data
    sign = hashlib.md5(key.encode()).hexdigest()
    print(sign)
    cs = str(data).replace(' ', '')
    from urllib.parse import quote
    uc = quote(cs)
    head.update({'cookie': '__ysuid=1595295517957qtr; UM_distinctid=179ad2304e5645-0d364787900664-45410429-1fa400-179ad2304e65bb; cna=Z7fyGAioincCAa8GBuIP+8Cl; __aysid=16221074248423BW; modalFrequency={"UUID":"10"}; xlly_s=1; redMarkRead=1; youku_history_word=%5B%22love%25253D1%22%2C%22love%253D1%22%2C%22%25E4%25B8%2580%25E4%25B8%258D%25E5%25B0%258F%25E5%25BF%2583%25E6%258D%25A1%25E5%2588%25B0%25E7%2588%25B1%22%5D; __ayft=1622164283883; __ayscnt=1; __guid=123717915.26848635123743390.1622169488316.636; ypvid=16221727234247TThTC; yseid=1622172723425czsbiH; ysestep=1; yseidcount=1; yseidtimeout=1622179923426; ycid=0; ystep=1; juid=01f6ogeq752vvv; referhost=https%3A%2F%2Fwww.so.com; seid=01f6ogeq772vql; seidtimeout=1622174523432; monitor_count=12; _m_h5_tk=' + cks + '; _m_h5_tk_enc=' + cksn + '; __arpvid=1622183701740ANqGwV-1622183701761; __aypstp=5; __ayspstp=16; P_ck_ctl=A3354B81253329781D7370B80C5B6BA8; isg=BM_PErd683Yib_cVtCvV8pYHXmPZ9CMWAt-N3eHbIT4wsOSy6cXIZJ6ysOAO0_uO; tfstk=c_yPBIvBMTBrXfDC6YMeVmqi5RZRwWquxKosZSJPpcYza0f0Len0cqoqA8vmZ; l=eB_bM0dcjkvvxHQzBOfanurza77OSIRYYuPzaNbMiOCP_DCB5Y9NW6_x-O86C3GVh6zJR3R4FBTTBeYBqQAonxvTqueTiSDmn'})
    url = 'https://acs.youku.com/h5/mtop.youku.soku.yksearch/2.0/?jsv=2.5.1&appKey=23774304&t=' + str(
        t) + '&sign=' + sign + '&api=mtop.youku.soku.yksearch&type=originaljson&v=2.0&ecode=1&dataType=json&jsonpIncPrefix=headerSearch&data=' + uc
    q = res.get(url=url, headers=head).json()
    time.sleep(random.randint(3, 10))
    print(q)
    try:
        if q['data']['nodes'] != []:
            page+=1
            print(page)
            start(page)
        else:
            return
    except Exception as e:
        save(t,sign,data)
        start(page)
start(2)