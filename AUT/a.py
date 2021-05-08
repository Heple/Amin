import openpyxl
import requests
import datetime
head = {
    'cookie': 'PHPSESSID=11',
    'x-requested-with': 'XMLHttpRequest',
}
csline = int(open('cslin.txt', 'r').readline())
line = int(open('lin.txt', 'r').readline())
ZB = ['张家界周玉双', '张家界冬子', '张家界郭梦', '张家界王胜', '张家界刘敏杰', '张家界王广兰', '张家界赵薇', '张家界王晓芳', '张家界刘洋洲']
csZB = ['张家界文敏', '张家界林纯君', '张家界庄勤璇', '张家界陈奕丝', '张家界马学彬', '张家界燕虹', '张家界敏玲', '张家界奕丹', '张家界卓凯生']
data = datetime.date.today()
oneday = datetime.timedelta(1)
print('输入1昨天2前天其他自定义')
i = input()
if i == '1':
    today = data - oneday
elif i == '2':
    today = data - oneday - oneday
else:
    today = input()

def K_F(serverid, num, wbk, li):
    if serverid == '' or num == 0:
        return
    else:
        print('F' + str(li))
        pre = wbk['F' + str(li)].value
        print(pre)
        price = float(pre) * int(num)
        print(price)
        ul = 'https://erp.lm12301.com/lvmeng.php/customer/customerservice/validlogadd?uid=%s&dialog=1' % serverid
        data = {
            'row[id]': '',
            'row[valid_date]': today,
            'row[valid_fans]': num,
            'row[valid_price]': '0.00',
            'row[valid_total_price]': '%s' % str(price)
        }
        res = requests.post(url=ul, headers=head, data=data)
        print(res.text)
def a(name):
    index = 0
    out = 0
    user = ''
    url = 'https://erp.lm12301.com/lvmeng.php/customer/customfriend/index?sort=create_time&order=desc&offset=0&limit=50&filter={"serviceuser.name":"' + name + '","request_time":"' + str(
        today) + ' 00:00:00 - ' + str(
        today) + ' 23:59:59"}&op={"serviceuser.name":"LIKE %...%","request_time":"RANGE"}&_='
    res = requests.get(url, headers=head).json()
    if res['rows'] == []:
        return index, out, user
    else:
        user = res['rows'][0]['service_uid']
    for i in res['rows']:
        if i['source'] == '被动手机号' and i['tag'] == []:
            index += 1
        else:
            out += 1
    return index, out, user

def ex():
    cswbs = openpyxl.load_workbook(r'C:\Users\Administrator\Desktop\2021数据\2021年潮汕精英广告投放加粉效果总统计.xlsx', data_only=True)
    cswsas = cswbs['5月广告效果']
    for i in range(0, len(csZB)):
        reurs = a(csZB[i])
        print(reurs)
        K_F(ddata(reurs), ydata(reurs), cswsas, csline)
    cswbs.close()
    wbs = openpyxl.load_workbook(r'C:\Users\Administrator\Desktop\2021数据\2021年广告投放加粉效果总统计.xlsx', data_only=True)
    wsas = wbs['5月广告效果']
    for i in range(0, len(ZB)):
        reurs = a(ZB[i])
        print(reurs)
        K_F(ddata(reurs), ydata(reurs), wsas, line)
    wbs.close()
def ydata(da):
    return da[0]


def ndata(da):
    return da[1]


def ddata(da):
    return da[2]

ex()
def savelin():
    open('lin.txt', 'w').write(str(line + len(ZB)))
    open('cslin.txt', 'w').write(str(csline + len(csZB)))
savelin()