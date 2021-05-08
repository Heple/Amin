import requests
import openpyxl
import datetime

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
print('潮汕花费')
csconst = float(input())
print('花费')
const = float(input())
csline = int(open('cslin.txt', 'r').readline())
line = int(open('lin.txt', 'r').readline())
head = {
    'cookie': 'PHPSESSID=11',
    'x-requested-with': 'XMLHttpRequest',
}
ZB = ['张家界周玉双', '张家界冬子', '张家界郭梦', '张家界王胜', '张家界刘敏杰', '张家界王广兰', '张家界赵薇', '张家界王晓芳', '张家界刘洋洲']
csZB = ['张家界文敏', '张家界林纯君', '张家界庄勤璇', '张家界陈奕丝', '张家界马学彬', '张家界燕虹', '张家界敏玲', '张家界奕丹', '张家界卓凯生']

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

def ydata(da):
    return da[0]


def ndata(da):
    return da[1]


def ddata(da):
    return da[2]

def zb_itrm():
    wb = openpyxl.load_workbook(r'C:\Users\Administrator\Desktop\2021数据\2021年广告投放加粉效果总统计.xlsx')
    wsa = wb['5月广告效果']
    wsa['D' + str(line)] = const
    for i in range(0, len(ZB)):
        reurs = a(ZB[i])
        sum = int(line) + i
        wsa['G' + str(sum)] = ydata(reurs)
        wsa['H' + str(sum)] = ndata(reurs)
    wb.save(r'C:\Users\Administrator\Desktop\2021数据\2021年广告投放加粉效果总统计.xlsx')
    wb.close()
    print('保存成功')


def cs_itm():
    cswb = openpyxl.load_workbook(r'C:\Users\Administrator\Desktop\2021数据\2021年潮汕精英广告投放加粉效果总统计.xlsx')
    cswsa = cswb['5月广告效果']
    cswsa['D' + str(csline)] = csconst
    for i in range(0, len(csZB)):
        reurs = a(csZB[i])
        sum = int(csline) + i
        cswsa['G' + str(sum)] = ydata(reurs)
        cswsa['H' + str(sum)] = ndata(reurs)
    cswb.save(r'C:\Users\Administrator\Desktop\2021数据\2021年潮汕精英广告投放加粉效果总统计.xlsx')
    cswb.close()
    print('保存成功')

def execl_main():
    zb_itrm()
    cs_itm()

execl_main()

