import json

import requests
import re
print('出行时间:')
tm=input()
print('出行地点:')
s_location=input()
print('抵达地点:')
e_location=input()
from fake_useragent import UserAgent
ua=UserAgent()
s_ciry_code=''
e_ciry_code=''
rest=requests.Session()
#113.238.142.208:3128
procy={
    'https':'139.9.25.69:3128'
}
city = {"北京": "BJS","上海": "SHA", "广州": "CAN","深圳": "SZX",
                     "成都": "CTU","杭州": "HGH", "武汉": "WUH","西安": "SIA","重庆": "CKG",
                     "青岛": "TAO","长沙": "CSX","南京": "NKG","厦门": "XMN","昆明": "KMG",
                     "大连": "DLC","天津": "TSN","郑州": "CGO","三亚": "SYX","济南": "TNA",
                     "福州": "FOC"
                     }
try:
    s_ciry_code=city[s_location]
    e_ciry_code=city[e_location]
except Exception:
    print('暂无该地点')
url='https://flights.ctrip.com/international/search/api/search/batchSearch'
baseheaders={
    'scope': 'd',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://flights.ctrip.com/international/search/oneway-'+s_ciry_code+'-'+e_ciry_code+'?depdate='+tm+'&cabin=y_s_c_f&adult=1&child=0&infant=0&containstax=1',
    'user-agent':ua.random,
}
oneway_url='https://flights.ctrip.com/international/search/oneway-'+s_ciry_code+'-'+e_ciry_code+'?depdate='+tm+'&cabin=y_s_c_f&adult=1&child=0&infant=0&containstax=1'
oneway_data=rest.get(url=oneway_url,headers=baseheaders,proxies=procy)
js=json.loads(re.search(r'{"adultCount":.*?\s',oneway_data.text).group(0).replace(';',''))
transactionID=js['transactionID']
print(transactionID)
import hashlib
key = transactionID+s_ciry_code+e_ciry_code+tm
sige = hashlib.md5()
sige.update(key.encode('utf-8'))
re = sige.hexdigest()
print(re)
baseheaders.update({'sign':str(re),'transactionid':str(transactionID),'content-type': 'application/json;charset=UTF-8'})
print(js)
fight=rest.post(url=url,headers=baseheaders,data=json.dumps(js),proxies=procy).json()
fightlist=[]
try:
    fightlist=fight['data']['flightItineraryList']
except Exception:
    print('更换IP重试')
for i in fightlist:
    aircraftName=i['flightSegments'][0]['flightList'][0]['aircraftName']
    departureDateTime=i['flightSegments'][0]['flightList'][0]['departureDateTime']
    arrivalDateTime=i['flightSegments'][0]['flightList'][0]['arrivalDateTime']
    flightNo=i['flightSegments'][0]['flightList'][0]['flightNo']
    price=i['priceList'][0]['adultPrice']
    print(str(aircraftName)+'--'+str(flightNo)+'----------'+str(departureDateTime)+'----'+str(arrivalDateTime)+'        最低价格：'+str(price))
