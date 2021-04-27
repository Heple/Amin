from PIL import Image
import base64
import requests
from io import BytesIO
sa=requests.Session()
dataa={
   's=/captcha'
}
head={
'cookie':'PHPSESSID=',
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
"username": "",
"password": "",
"captcha": capt
}
# ck=requests.utils.dict_from_cookiejar(sa.cookies)
# print(ck['PHPSESSID'])

lg=requests.post(url=log,headers=head,data=data)
print(lg.text)