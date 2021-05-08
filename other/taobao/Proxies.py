import redis

proxies = {
    'http': '',
}
proxies_s = {
    'https': ''
}
PROXIES_HTTP = 'proxies_http.txt'
PROXIES_HTTPS = 'proxies_https.txt'
prourl = 'http://www.ip3366.net/?stype=1&page={}'
from lxml import etree
import requests
import os
import time
import random

proxies_1 = {
    'http': '',
    'https': ''
}
http = []
https = []
proxies_http = {'http': ''}
proxies_https = {'https': ''}
testipul = 'http://httpbin.org/ip'
testipuls = 'https://httpbin.org/ip'
xilaul = 'http://www.xiladaili.com/'
test_http = []
test_https = []
conn = redis.Redis(host='127.0.0.1', port=6379,decode_responses=True)


class Proxies:

    def checkip(self, procy):

        heads = {
            'referer': 'http://httpbin.org',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

        try:
            res = requests.get(url=testipul, headers=heads, proxies=procy, timeout=1)
            print(res.status_code)
            http.append(procy['http'])
            return True
        except Exception:
            return False

    def checkips(self, procy):

        heads = {
            'referer': 'https://httpbin.org',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        try:
            res = requests.get(url=testipuls, headers=heads, proxies=procy, timeout=1)
            print(res.content)
            print(res.status_code)
            https.append(procy['https'])
            return True
        except Exception:
            return False

    def xiladali(self):

        head = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            'Host': 'www.xiladaili.com'}
        try:
            res = requests.get(url=xilaul, headers=head)
        except Exception as e:
            raise e
        html = etree.HTML(res.text)
        for i in range(1, 6):
            try:
                ips = html.xpath(f'/html/body/div/div[3]/div[1]/table/tbody/tr[{i}]/td[1]/text()')
                proxies_https['https'] = ips[0]
                print('xila:', proxies_https)
                self.checkips(proxies_https)
            except Exception:
                break

        for i in range(1, 10):
            try:
                ip = html.xpath(f'/html/body/div/div[3]/div[2]/table/tbody/tr[{i}]/td[1]/text()')
                proxies_http['http'] = ip[0]
                print('xila', proxies_http)
                self.checkip(proxies_http)
            except Exception:
                break

    def yundaili(self, num):

        head = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
            'Referer': 'http://www.ip3366.net/'}

        for i in range(1, num):
            time.sleep(random.randint(3, 10))
            res = requests.get(url=prourl.format(i), headers=head)
            html = etree.HTML(res.text)
            for i in range(1, 10):
                ip = html.xpath(f'//*[@id="list"]/table/tbody/tr[{i}]/td[{1}]/text()')
                prox = html.xpath(f'//*[@id="list"]/table/tbody/tr[{i}]/td[{2}]/text()')
                sl = html.xpath(f'//*[@id="list"]/table/tbody/tr[{i}]/td[{4}]/text()')
                if sl[0] == 'HTTP':
                    proxies_http['http'] = str(ip[0]) + ':' + str(prox[0])
                    print('yun', proxies_http)
                    self.checkip(proxies_http)
                elif sl[0] == 'HTTPS':
                    proxies_https['https'] = str(ip[0]) + ':' + str(prox[0])
                    print('yun', proxies_https)
                    self.checkips(proxies_https)

    def nimadaili(self, num):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://www.nimadaili.com/https/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        for i in range(1, num):
            https_proxy_url = f"http://www.nimadaili.com/https/{i}/"
            resp = requests.get(url=https_proxy_url, headers=headers).text
            tree = etree.HTML(resp)
            https_ip_list = tree.xpath('/html/body/div/div[1]/div/table//tr/td[1]/text()')
            for ip in https_ip_list:
                proxies_https['https'] = ip
                self.checkips(proxies_https)
            print('Redis数据库有HTTPS代理IP数量为：', conn.smembers('https'))

    def saveProxies(self):
        print(https)
        [conn.sadd('http', ip) for ip in http]
        [conn.sadd('https', ip) for ip in https]
        # with open(PROXIES_HTTP, 'w+', encoding='utf-8') as file:
        #     for i in http:
        #         j=file.readlines()
        #         if i not in j:file.write(str(i) + '\n')
        #     file.close()
        # with open(PROXIES_HTTPS, 'w+', encoding='utf-8') as file:
        #     for i in https:
        #         j = file.readlines()
        #         if i not in j:file.write(str(i) + '\n')
        #     file.close()

    def Now_Proies(self):
        ips = conn.smembers('https')
        for i in ips:
            proxies_https['https']=i
            print(proxies_https)
        #     with open(PROXIES_HTTP, 'r', encoding='utf-8') as file:
        #         r = file.readlines()
        #         for i in r:
        #             i = i.replace('\n', '')
        #             proxies_http['http'] = i
        #             print(proxies_http)
        #             if self.checkip(proxies_http):
        #                 print('我可用')
        #                 test_http.append(i)
        #         file.close()
        # with open(PROXIES_HTTPS, 'r', encoding='utf-8') as file:
        #     r = file.readlines()
        #     for i in r:
        #         i = i.replace('\n', '')
        #         proxies_https['https'] = i
        #         print(proxies_https)
        #         if self.checkips(proxies_https):
        #             print('可用')
        #             test_https.append(i)
        #     file.close()

    # print('可用个数:', len(test_http) + len(test_https))
    # if len(test_http) + len(test_https) < 10:
    #     print('没有收集到那么多ip')
    #     return False
    # print('收集到了')
    # return True


def removeproixes(self):
    os.remove(PROXIES_HTTP)
    os.remove(PROXIES_HTTPS)


def init_proxies(self):
    proxies['http'] = proxies_http[random.randint(0, len(proxies_http) - 1)]
    proxies_s['https'] = proxies_https[random.randint(0, len(proxies_https) - 1)]


if __name__ == '__main__':
    pr = Proxies()
    # if not pr.Now_Proies():
    #     pr.removeproixes()
    pr.nimadaili(5)
    # pr.yundaili(3)
    # pr.xiladali()
    # pr.saveProxies()
    pr.Now_Proies()
