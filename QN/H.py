import os
import threading
import requests
import re
import execjs
from Crypto.Cipher import AES
from Crypto.SelfTest.st_common import a2b_hex

baseurl='https://vip5.3sybf.com'
head={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
ul='http://www.avtt859.com/shipin1/ribenwuma/play_10101617_1.html'
res=requests.get(url=ul,headers=head)
res.encoding='utf-8'
os.environ["EXECJS_RUNTIME"] = "JScript"
j1=res.text.replace('<script>document.write','')
j2='b='+j1.replace('</script>','')
print(j2)
if not os.path.exists(r'C:\\Users\\Administrator\\Desktop\\QW'):
    os.makedirs(r'C:\\Users\\Administrator\\Desktop\\QW')
resulr=execjs.compile(j2)
d=resulr.eval('b')
#f=open('js.txt','r',encoding='utf-8').read()
rep=re.search('Base64.decode(.*);',d).group(1)
reps=rep.replace('("','').replace('"))','')
import base64
url=base64.b64decode(reps).decode('utf-8')
r2=requests.get(url=url,headers=head).text
print(r2)
nul=re.search('RESOLUTION=1280x720\n(.*)',r2).group(1)
mainul=baseurl+nul
print(mainul)
def Aeskey():
    r3=requests.get(url=mainul,headers=head).text
    keyurl=baseurl+re.search('URI="(.*)"',r3).group(1)
    print(keyurl)
    aeskey=requests.get(url=keyurl,headers=head).content
    print(aeskey)
    crytor=AES.new(aeskey,AES.MODE_CBC,aeskey)
    sumulist=re.findall('(.*.ts)',r3,re.M)
    print(len(sumulist))
    ts=[]
    fn=0
    for i in range(0,len(sumulist),300):
        lists=sumulist[i:i+300]
        thing=threading.Thread(target=start_down,name='vth-'+ str(i),kwargs={'flename':fn,'sumulist':lists,'crytor':crytor})
        thing.setDaemon(True)
        ts.append(thing)
        fn+=300
    print('线程数',len(ts))
    for i in ts:
        i.start()
    for i in ts:
        i.join()
def start_down(flename,sumulist,crytor):
    fl=0
    fl+=flename
    flna = r'C:\\Users\\Administrator\\Desktop\\QW\\' + str(fl)
    if not os.path.exists(flna):
        os.makedirs(flna)
    fileover(flna,fl)
    for i in sumulist:
        fl += 1
        mpcontent = requests.get(baseurl + i)
        with open(flna+r'\\'+str(fl) + '.ts', 'ab+')as fs:
            print('下载',i)
            fs.write(crytor.decrypt(mpcontent.content))
            fs.flush()
    os.system(r'cd '+flna+'&&'+'q.bat')
def fileover(flna,fl):
    bat='@echo off & setlocal enabledelayedexpansion \n for %%a in (*.ts) do set /a count+=1 \n for /l %%a in ('+str(fl+1)+',1,'+str(fl+300)+') do (\n if not defined num (\n set num=%%a.ts) else (\n set num=!num!+%%a.ts)) \n copy /b !num! '+r'C:\\Users\\Administrator\\Desktop\\QW\\'+str(fl)+'.ts'
    open(flna+r'\\q.bat','w').write(bat)
def filesum():
    bat ='@echo off & setlocal enabledelayedexpansion \n for %%a in (*.ts) do set /a count+=1 \n set /a res=%count%*300 \n for /l %%a in (0,300,!res!) do (\n if not defined num (\n set num=%%a.ts) else (\n set num=!num!+%%a.ts)) \n copy /b !num! ' + r'C:\\Users\\Administrator\\Desktop\\QW\\' + 'SB.mp4'
    open(r'C:\\Users\\Administrator\\Desktop\\QW\\q.bat', 'w').write(bat)
    os.system(r'cd C:\\Users\\Administrator\\Desktop\\QW&&C:\\Users\\Administrator\\Desktop\\QW\\q.bat')
    os.startfile(r'C:\\Users\\Administrator\\Desktop\\QW')
Aeskey()
filesum()