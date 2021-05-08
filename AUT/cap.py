from PIL import Image
import base64
import requests
from io import BytesIO
sa=requests.Session()
#files={'image':('test.png',open('127.jpg','rb'),'image/png')}
dataa={
   's=/captcha'
}
head={
'cookie':'PHPSESSID=11',
'x-requested-with': 'XMLHttpRequest'
}

res=requests.get("https://erp.lm12301.com/index.php?s=/captcha",headers=head)
by=res.content
s=BytesIO(by)
img=Image.open(s)
img.save('cap.png')
img.show()
log='https://erp.lm12301.com/lvmeng.php/index/login'
print("验证码:")
capt=input()
data={
"__token__": "",
"username": "csxfy:tuiguang",
"password": "123456",
"captcha": capt
}
# ck=requests.utils.dict_from_cookiejar(sa.cookies)
# print(ck['PHPSESSID'])
heads={
   'cookie':'PHPSESSID=11',#+ck['PHPSESSID'],
   'x-requested-with': 'XMLHttpRequest'
}
lg=requests.post(url=log,headers=heads,data=data)
print(lg.text)