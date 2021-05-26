import json

import requests
from io import BytesIO
from PIL import Image
from fake_useragent import UserAgent
ua=UserAgent()
ul='https://flight.qunar.com/touch/api/domestic/wbdflightlist?departureCity=长沙&arrivalCity=深圳&departureDate=2021-04-23&ex_track=&__m__=7a5ad06e22c644ddd05679814b31a99b&st=1618971220228&sort=&_v=4'
res=requests.Session()
logul='https://user.qunar.com/webApi/logins.jsp'
capul='https://user.qunar.com/captcha/api/image?k={en7mni(z&p=ucenter_login&c=abc&t=1618972076264'
def log():
    head = {
        'referer': 'https://flight.qunar.com/site/oneway_list.htm',
        'user-agent': ua.random
    }
    re = res.get(url=capul, headers=head)
    s = BytesIO(re.content)
    img = Image.open(s)
    img.save('cap.png')
    img.show()
    print('请输入验证码:')
    im = input()
    data = {
        'username': '17670457110',
        'password': 'qw124563264583',
        'remember': '1',
        'prenum': '86',
        'isHalfLogin': 'false',
        'vcode': str(im)
    }
    print(res.cookies)
    ck = requests.utils.dict_from_cookiejar(res.cookies)
    res.cookies = ck
    print(res.cookies)
    savecookie()
    initcookie()
    print(res.cookies)
    start=res.post(url=logul, headers=head, data=data)
    if start.status_code==200:print('登录成功')
    sck=requests.utils.dict_from_cookiejar(res.cookies)
    res.cookies=sck
    savecookie()


import random
def a(e):
    t='123456789poiuytrewqasdfghjklmnbvcxzQWERTYUIPLKJHGFDSAZXCVBNM'
    n=''
    for i in range(0,e):
        b=(random.random()*1e8)%float(len(t))
        n=t[int(b)]+n
    return n

def loginok():
    userul = 'https://user.qunar.com/index/basic?csrfToken='+a(32) +'&t='
    head={
        #'cookie':'QN1=00007180039831b1d2c8f3e7;QN25=daaf7c64-9cac-4594-9bad-ec6ad8b4b8c6-9f992f90;csrfToken=UovWmCb8MhpP9rRIhF8156JSs4DyQPrA',
        'referer':'https://user.qunar.com/userinfo/account.jsp',
        'user-agent':ua.random
    }
    initcookie()
    re=res.get(url=userul,headers=head)
    if re.json()['errcode'] !=200:
        print('登录过期')
        return False
    else:
        print('欢迎回来: '+re.json()['data']['username'])
        return True

def savecookie():
    with open('cook.txt', 'w+', encoding='utf-8') as file:
        json.dump(res.cookies, file)
        print('保存cookies文件成功！')

def initcookie():
    with open('cook.txt', 'r+', encoding='utf-8') as file:
        cookies_dict = json.load(file)
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        res.cookies = cookies
#log()
loginok()