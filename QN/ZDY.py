import re
import requests,hashlib
import time
from lxml import etree


headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'text/plain, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.zdaye.com/FreeIPList.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}



def MD5(p):
    return hashlib.md5((p).encode()).hexdigest().upper()

def sdfsgfdg(s):
    s2 = s.split('m')
    ts = ''
    for i in range(len(s2)-1,-1,-1) :
        ts += chr(int(s2[i])-352)
    return ts

def dsfgsd(s, kk):
    s2 = s.split("#")
    ts = ""
    for i in range(len(s2)-1,-1,-1):
        ts += chr(int(s2[i])-kk)
    return ts

def get_keyUrl(mk,ak):
    url = "https://www.zdaye.com"+"/" + mk + "_" + MD5(MD5(sdfsgfdg(mk) + "beiji" + ak)) + ".gif"
    return url


session = requests.session()
res = session.get('https://www.zdaye.com/FreeIPList.html',headers=headers).text


selector = etree.HTML(res)
trs = selector.xpath('//*[@id="ipc"]/tbody/tr')
ip_infos = []
for tr in trs:
    ip_1 = tr.xpath('./td[1]/text()')[0]
    ip_2 = tr.xpath('./td[1]/@v')[0]
    ip_infos.append((ip_1,ip_2))
print('解密前:',ip_infos)


t = str(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())).replace(' ','%20').replace('/0','/')
url = 'https://www.zdaye.com/js/base.js?'+t
print(url)
pp = session.get(url,headers=headers).text
mk = re.findall('mk = "(.*?)"',pp)[0]
ak = re.findall('ak = "(.*?)"',pp)[0]
print(mk,ak)

key_url = get_keyUrl(mk,ak)
print(key_url)

key = session.get(key_url,headers=headers).text
print('解密得key:',key)


ip_new = []
for info in ip_infos:
    ip = info[0].replace('wait',dsfgsd(info[1],int(key)))
    ip_new.append(ip)
print('解密后:',ip_new)