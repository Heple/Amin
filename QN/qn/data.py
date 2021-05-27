import json
import random

import requests
from io import BytesIO
from PIL import Image
from fake_useragent import UserAgent
import execjs
import re
import time
ua = UserAgent()
print('出发地:')
st=input()
print('到达地:')
dat=input()
print('出行时间:')
tm=input()
print('返程时间:')
outtm=input()
testipul = 'http://httpbin.org/ip'
testipuls = 'https://httpbin.org/ip'
mul='https://m.flight.qunar.com/flight/api/touchInnerList'
url='https://flight.qunar.com/flight/api/wwwInnerList'
baseurl='https://flight.qunar.com/site/oneway_list.htm'
res = requests.Session()
_s=''
_q=''
_u=''
with open('cook.txt', 'r', encoding='utf-8') as file:
    cookies_dict = json.load(file)
    _s = cookies_dict['_s']
    _q=cookies_dict['_q']
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    res.cookies = cookies
    file.close()

print(_s)
print(_q)
print(_u)
head = {
    'referer': 'https://flight.qunar.com/site/oneway_list.htm',
    'pre': '2b597070-49b326-6846cb84-72937c95-0d4a3c6080fb',
    'user-agent': ua.random,
}
data={
'b[allFilters]': '[]',
'b[depCity]': st,
'b[arrCity]': dat,
'b[goDate]': tm,
'b[backDate]': outtm,
'b[underageOption]': '',
'b[roundTripType]': 'go',
'b[sortType]': '1',
'c[ke]': '13800138000',
'c[cid]':'qunar',
'c[vid]':'93010001',
'c[pid]': '10060',
'c[uid]': '000079002f1031bd06302c23',
'c[t]': 'f_flight_rn_domestic_flightlist',
'c[qcookie]': _q,
'c[vcookie]':'',
'c[tcookie]': '27098480',
'c[scookie]': _s,
'c[openId]':' ',
'c[unionId]':'',
'c[un]': _u
}
key=res.get(url=baseurl,headers=head)
jslod=re.search('<script>var (.*)</script>',key.text).group(1)
keylist=re.findall("\)]='(.*?)'",jslod)
print(keylist)
Klist=[]
Klist.append(keylist[1])
Klist.append(keylist[2])
Klist.append(keylist[3])
Klist.append(keylist[4])
Klist.append(keylist[5])
Klist.append(keylist[6])
Klist.append(keylist[7])
print(Klist)
stt=''
for i in Klist:
    stt=stt+'"'+i+'",'
print(stt)
jsjile=open('../pt.js', 'r').read()
js='var a=['+stt+']\n'+jsjile
print(js)
resulr=execjs.compile(js)
pt=resulr.eval('re')
print(pt)
def a(e):
    t = '123456789poiuytrewqasdfghjklmnbvcxzQWERTYUIPLKJHGFDSAZXCVBNM'
    n = ''
    for i in range(0, e):
        b = (random.random() * 1e8) % float(len(t))
        n = t[int(b)] + n
    return n
headers={
    'pre': pt,
    'referer': 'https://flight.qunar.com/site/roundtrip_list_new.htm',
    'user-agent': ua.random
}
rep = res.post(url=url, headers=headers,data=data)
print(rep.text)

