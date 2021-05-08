import requests
import json
import openpyxl
import re
import datetime
sayurl = 'https://erp.lm12301.com/lvmeng.php/customer/customfriend/searchtalk'
tab_url = 'https://erp.lm12301.com/lvmeng.php/customer/customfriend/edit'
print('输入1今天2昨天其他自定义')
data=datetime.date.today()
oneday=datetime.timedelta(1)
a=data-oneday
head = {
    'cookie': 'PHPSESSID=11',
    'x-requested-with': 'XMLHttpRequest',
}
get=str(input())
time=get=='1'
print(time)
if get=='1':
    starttime = str(data)
    endtime = str(data)
elif get=='2':
    starttime = str(a)
    endtime = str(a)
else:
    starttime=str(input())
    endtime=str(input())
from_id = ""
print(starttime)
tag_id = []
def datas(frome):
    saydata = {
        'start_time': '',
        'end_time': '',
        'keyword': '',
        'type': '',
        'friend_id': frome,
        'log_id': '',
        'page_size': '30',
        'page_type': ''
    }
    return saydata


tagdata = {
    'tags_text: '
    'tags: 5'
    'id': '1692'
}
list_le = ""
frome_id = []
list_id = []
def S_X(Str):
    if '广告推广' in Str or '小伙伴' in Str or '无聊人群' in Str or '客户分享名片' in Str:
        return False
    return True

def F_T(startime, endtime,off):
    global list_le, tag, name, i
    listurl = 'https://erp.lm12301.com/lvmeng.php/customer/customfriend/index?sort=create_time&order=desc&offset='+str(off)+'&limit=50&filter={"request_time":"' + startime + ' 00:00:00 - ' + endtime + ' 23:59:59"}&op={"request_time":"RANGE"}&_='
    listtxt = requests.get(listurl, headers=head).text
    js = json.loads(listtxt)
    jp=js['rows']
    print(jp)
    print(frome_id)
    if jp!=[]:
        for i in js['rows']:
            list_le = i['source']
            name = i['serviceuser']['name']
            tag = i['tag_name']
            if S_X(tag):
                if list_le == "被动手机号":
                    frome_id.append(i['from_id'])
                    list_id.append(i['id'])
#                    K_F(str(name), 3)
                else:
                    pass
#                    K_F(str(name), 2)
        off+=50
        F_T(startime,endtime,off)
F_T(starttime,endtime,0)

# def flatten(a):
#    if not isinstance(a, (list,)):
#       return [a]
#    else:
#       b = []
#       for item in a:
#          b += flatten(item)
#    return b

def set_tab(id, tab_id):
    id = str(id)
    data = {
        'tags_text': '',
        'tags': tab_id,
        'id': id
    }
    just = requests.post(tab_url + '?id=' + id + '&dialog=1', headers=head, data=data)
    print(just.text)


def start():
    is_send = 0
    index = 0
    print(frome_id)
    for i in frome_id:
        i = str(i)
        saylist = json.loads(requests.post(sayurl, headers=head, data=datas(i)).text)
        say_list = saylist['data']['msg_log_list']
        print(say_list)
        for j in say_list:
            if (j['is_send'] == 0):
                is_send += 1
                name = j['nickname']
                if name==None:
                    is_send-=1
        print('回复条数:' + str(is_send))
        if (is_send < 2):
            set_tab(list_id[index], "5")
            print(list_id[index])
        else:
            set_tab(list_id[index], "")
        is_send = 0
        index += 1

start()
