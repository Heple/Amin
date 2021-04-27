import pandas as pd
import requests
import re
import json
import os
import Proxies
import random
res=requests.Session()
COOKIES_FILE_PATH = '../../../../Erp/taobao_cookies.txt'
my_taobao_url = 'http://i.taobao.com/my_taobao.htm'


def testcookies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    if not os.path.exists(COOKIES_FILE_PATH):
        return False
    with open(COOKIES_FILE_PATH, 'r+', encoding='utf-8') as file:
        cookies_dict = json.load(file)
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        res.cookies=cookies
        print(res.cookies)
    try:
        response = res.get(my_taobao_url, headers=headers,proxies=Proxies.proxies)
        print(response.text)
    except Exception as e:
        print('获取淘宝主页请求失败！原因：')
        return False
    nick_name_match = re.search(r'<input id="mtb-nickname" type="hidden" value="(.*?)"/>', response.text)
    if nick_name_match:
        print('登录淘宝成功，你的用户名是：{}'.format(nick_name_match.group(1)))
        print(res.cookies)
        return True
    else:
        os.remove(COOKIES_FILE_PATH)
        print('登录失败,尝试再次登录')
        return False

class Login:

    def __init__(self,s):
        ualist=['-','+','=']
        ua=''
        self.s=s
        for i in range(random.randint(1,5)):ua=ua+ualist[random.randint(0,i)]
        print(ua)
        self.vst_url = 'https://login.taobao.com/member/vst.htm?st={}'
        self.ul = 'https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0&_bx-v=2.0.32'
        self.thead = {
            'origin': 'https://login.taobao.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'referer': 'https://login.taobao.com/member/login.jhtml',
        }
        self.tdata = {
            'loginId': '17670457110',
            'password2': 'a8da33dbb098e82847bb33d02095591228ce46b9a2827def3b0a946191110bb3b59bf3caaaf6c92e3ac2cf382ad1ac4d52669c289b8c5f3c01b88b2c721ecac0f6938fb20cc785f4eb976b7c08600ec430e581ab555e744dc9a8e97442f8ef963c7ecc0822ca3d62dd03dfc137ac9f3db4a8fef3d09a02c66d5bbd81cc5b252c',
            'keepLogin': 'false',
            'ua': '140#b21rDhaJzzFkSzo23bib3pSXnT082cbSJyHeGV3He9lNHdMVqPyTEtzgtB1+D4L8zhyo2DzLn6hqzznTMYfeT4rzzFzMVY/ulFzx2DD3VthqzF+BqQ1SlpODzPzYVXE/lbcSHDdnDzbpONdOHaU+6h2oi+Hxz0IID1/GMU4zW8qSs4H74YU+6bKwEKoBN3DtowdEYgPYHgZHnPVtH+rCnZG/VCy6EL8O1rQWNmbnsdN64fzawhZkfCIlNE37njHNK/giBifjQBlo5/h3zsmk4Rzm14wifowuBOVW1jr4ASsb8al50H0EyY0M8ID3WDi4iSV3eYjZhCxSO4z9C0aEbe12BDW+UztpZGxzAi/PhxVUZk0QtWwX44PkuY7Q76iU4CtZaPaSOYlv2EtbzrzdSFhw3UaAv0J42c6UG/IP5xmqMRH379qHaSPo3IeAujjI+M4QxW8BhuKc74OwvZkzfF1xkeUS8eNg1fyNjUs5ibYHC1935DuFglm2BbpC2MsEMwuHegWAImlljUphFgMhFjHZ5Q8O1OsXohi4IQssWUeYPXadxr2rnpBjm8WTLiK/2auqb6lIlI/ndmYkGHM3SepGLrbkNFpVA9KnPfsifnmGyY9X2YeZ7cLZSBO6cqKZnowPcDiiiIZTrvGXsQMa9Sd1Cv86zRrBIR2AxZtht4G5Lyoo/n2KfpmPA+6pQAF7Wd1G3nFxl1AIlrzhzUR9yiK1L5fk94e4J4SMLje++8k5big4DmMVRjc3Km0lwDP0Ur2koENH08sDrsCtMXI9Wm2RTxRCz8bgXWzkqKJrfnoInvZdahgJKKmIsBwvae9XF7rN4XvFwR1nY7GBqxAkWkpRAazcIm8c/9uUh0gIGSkxwB8h/GGV0JDhL+NwhjHinC+YrQOiar1IQkRMW3wRRlHj/uXO6aOLO8v80ufWo/ecE8ImeO6ttAO1jOKrRYyP4ve6cQmFGxwzU6Knm2cvGlsSHHYCchRutMSeO/grYagDI36CQ71aSz/fdPaPqx6mQDTqYCS3a5JxjM032ONo/v+0A+xPfHmA+JTRMxReMOfARbPIPldnY8sMaJ7a59Hjk7BIBUi9EpXjX1TkYYfQrCqT5O2PkjhxAalRpiq1xYB/+81YBo9NzhIEAmWsrHwHXSueuF/a0wGcPmMq3MI72e1K2wQeZNvPKwpGm2RcG6UQRrJX77tv1OP0R/+XgD+Icu8AmJmS/4WFb4ufymFp5kpWcKZzfzdPE94EfLp2vI4EMr9738iLUIWcZaqyuZVvV4iEbr8A1Ay/NtpwdZWNBysfxdFG0e+M6W5mfqLITukWzplZNApxOVSU04nzwvAWaOVSts2/Ut29mCffGPHn/9TakdvYhoqHN6kVGZ0+U9ixFBbYOoJA6IF5'+ua,
            'umidGetStatusVal': '255',
            'screenPixel': '1920x1080',
            'navlanguage': 'zh-CN',
            'navPlatform': 'Win32',
            'appName': 'taobao',
            'appEntrance': 'taobao_pc',
            '_csrf_token': 'CHOCtLa4c3ca5dR8Q3mre4',
            'umidToken': '073019943c2c93f111f98c84b7c886827a97fbee',
            'hsiz': '14eff220fcfd0bf2fc286a1c5748261e',
            'bizParams': '',
            'style: default'
            'appkey: 00000000'
            'from: tbTop'
            'isMobile: false'
            'lang: zh_CN'
            'fromSite': '0',
            'bx-ua': '202!ttV MtIDCq8tjT d7yDmNomBkPX5Nty0IDEcSxyMMXdWX0vDwbPfNXPBkcU5vtyakj8CfPHqvWEcwlzN60ttNozxtNYB8 t0y8DtsbYE8NKatt0b/ZaN04KtNW0WxYI2tShtsAHN8tK0tW0b/sdEKKDpbeCX87WaKZDE/xd/A8BmV6jDsTREEBJEYHdamGK8RBjKYnRUzB35WNjWsIJUNfdNVHljAI34RDD7/vkvjtvatt0C/ZdNtM7ttxOd8 t00ByusgHE8MKytv0b/ 0pti4vcqm/993N7fyphCkdEiWbiWtP3Ds3SadfHoLM1skoCpC1QCyfms35TXjthQQoZnNiPxrY1skoK 0pHoyfms3jKQzpOQhXdDrars37DT3ZWyyXEMtdCDsZHDykDNe2xWDDr56wQw46WXTlX8Wtxx5BkBIv0N1 bBKJ0MgXQGj1lw7QCB9NfJ4Ha4m1aEZsjW7tlNgVt2/9N54kr4vQxa8HQ/ckVSJACEAdVtgetK66k4/KDrv6ex/ON42kQWhmRNg0jSPIlcc3WyyXr/wVxx/wUDgOW417Cy/3lL6Etdqvd8YhrM8Oay5Gd/1OaD4ZkWtHlh3QWnf6dwmIXM3OcKMtdgchwWdvkDmBrL5eXNLmtNFJYDydOlSI7nmp3vboEqLHbhM7dpfoKaDpHoDfmiIJlvSexbxlmYwqo7rUN1WvDYV3hAF 8hfnqrEAkhav8 H8DXZE2eUeAnjVlFM4p1ETBB9x0 hFqizMjJM6PrTxrgeDSxmoaQKi/HVT6T8px9YBW6r8EAn4N2d6W8KQJtytBS3Sl2zEeA5b8KD9WNdAdpLlbbr0BDWEPq4uPXB6BOS6T9aBCWbpQ8 NSpjjL1GkI0sffBxu33CQzo5Jyt2NXxIIkHglEpb/YE/7NH5wLPHmNXaEEKW2qY7HNEbZ4EmzA O4dJabv39klJXPmOYoFguCeF2LGz81x2wZUK3ayzaz lPchpy2WOYpTDPCEYJY2df9xgXEjkjnUD3MAaWPwebNDmFZAvPWOFfAWkZXQvAxKE5yiEqhxEbIx12YMwryieuy1NL99rndHdsQDHYiKg3JUE8FLgTYJVL0h3LxSLCFbg2y7z5g8dZDwKUr64Q5M0jho0DZQijhnb3vaTqwSmIF4o0ayr6NZomIqZYNe4mdLq9HmB8gTeldoH7OESYk5VtXA1SNt3tiV/OmsdOrrl/V46oLE/pFzNRTKCBKMR5a03t /QijI5ud3Vju7FgbJed2dcU58yHyro yuhvyGeU94eIHHobOdwgH8TTQsarx5Bvfd3AClaEY/BzfXKf2c5LhKL0M1pBZCMamvT7PuY3ACMEIGneU2ssZeLGiTCsJAUCWT7RqX ysl0JcehtBe9fJ/YhDNlBy6QLLJDtEdVge rQJrZHIvNejnWonTv1sfq2OoQfVMHE0iMkjyVIxrHqmCaxUu48bvpynF97ZMKj5Gx8sgs3NQTD diXmn0OS uH4D3FBmtt5TtLVjrAgN WHMzgF4aSmKdkNM5JSJNrLA92LqE3CLcSGcqHYU/qTf1/HdLwdp7 tch6kby7DvcTGIEapO6EAntC58wjmTWT5tuEOXPuL5uAcCfRmEN77qWpOV8/xgtyNcKc/Py/3uCFj2vfWbjKeBZ7JpoZXSpzEEZxwB9NpWwXjLYo24888C8VRw44ceSH3zcu/4u096drQ3LsHdl5tgR2qBANzA1WHNxyTYEHC1dJmJVTwO7lxFg4ya9meKu34q6DBzstcxAt7oDyIv39DQK3oBvkRkcGi 8M3JKDM0RcpndasWQbExiyrHzFdfgfeF6cD/A7IbcOXYgwtAMf89zn6Y2JAYyUrDkPPA1HvUaR9cJgQp8zB835OIMI6SUKxUlLlurPcXriIWY7f05nQ5tOkc5/kn9uE0ZFp6REBK Rkx3xx/pV13jwpsPy k2My7Xjaoz8dP1PqXb7if BocvHZLwJFQhWJm9lQlJXLTfS0D9/y9Ltro JVKl2MVNjDlPjAGlaWxq9NAVnGIHNGsHPWWTxLNJwdPeAnfqe0n/ms/tEuisDIBHzmsc/UXAmQKmNp09Y39qHRP4n012H znkZNHEZi pEqrEE6FBJ/BykDwzs3CmgksXydLPC8gLsxdCpXSJs',
            'bx-umidtoken': 'T2gAHNOBKW8J43_zfPeqAUkEIZ2BJ4XtjoukQkv_I_lAQY9yF91z-Mh7zLy2H7qScS8='
        }
    def getstpath(self):
        try:
            resq = self.s.post(url=self.ul, headers=self.thead, data=self.tdata,proxies=Proxies.proxies)
            apply_st_url_match = resq.json()['content']['data']['asyncUrls'][0]
        except Exception as e:
            print('验证用户名和密码请求失败，原因：')
            raise e
        return apply_st_url_match

    def getst(self):
        try:
            stres = self.s.get(self.getstpath(),proxies=Proxies.proxies)
            st_match = re.search(r'"data":{"st":"(.*?)"}', stres.text).group(1)
        except Exception as e:
            print('st码申请失败')
            raise e
        return st_match

    def st_login(self):
        shad = {
        'Host': 'login.taobao.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        try:
            self.s.get(self.vst_url.format(self.getst(),proxies=Proxies.proxies), headers=shad)
        except Exception as e:
            print('st码申请失败')
            raise e

    def setcookies(self):
        cookies_dict = requests.utils.dict_from_cookiejar(self.s.cookies)
        self.s.cookies=cookies_dict
        print(self.s.cookies)
        with open(COOKIES_FILE_PATH, 'w+', encoding='utf-8') as file:
            json.dump(self.s.cookies, file)
            print('保存cookies文件成功！')

if __name__ == '__main__':
    # if testcookies():
    #     pass
    # else:
        lg = Login(res)
        lg.getstpath()
        lg.setcookies()
        testcookies()