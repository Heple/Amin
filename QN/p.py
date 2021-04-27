import requests
import openpyxl
import datetime

data = datetime.date.today()
oneday = datetime.timedelta(1)
print('输入1昨天2前天其他自定义')
i = input()
print('花费')
const = input()
print('行数')
line = input()
print('潮汕花费')
csconst = input()
print('潮汕行数')
csline = input()
wb = openpyxl.load_workbook(r'C:\Users\Administrator\Desktop\2021数据\2021年广告投放加粉效果总统计.xlsx',data_only=True)
wsa = wb['4月广告效果']
cswb = openpyxl.load_workbook(r'C:\Users\Administrator\Desktop\2021数据\2021年潮汕精英广告投放加粉效果总统计.xlsx',data_only=True)
cswsa = cswb['4月广告效果']
if i == '1':
    today = data - oneday
elif i == '2':
    today = data - oneday - oneday
else:
    today = input()
head = {
    'cookie': 'PHPSESSID=',
    'x-requested-with': 'XMLHttpRequest',
}
ZB = ['张家界周玉双', '张家界冬子', '张家界郭梦', '张家界王胜', '张家界刘敏杰', '张家界王广兰', '张家界赵薇', '张家界王晓芳', '张家界刘洋洲']
csZB = ['张家界文敏', '张家界林纯君', '张家界庄勤璇', '张家界陈奕丝', '张家界马学彬', '张家界燕虹', '张家界敏玲', '张家界奕丹', '张家界卓凯生']
def a(name):
    index = 0
    out = 0
    user=''
    url = 'https://erp.lm12301.com/lvmeng.php/customer/customfriend/index?sort=create_time&order=desc&offset=0&limit=50&filter={"serviceuser.name":"' + name + '","request_time":"' + str(
        today) + ' 00:00:00 - ' + str(
        today) + ' 23:59:59"}&op={"serviceuser.name":"LIKE %...%","request_time":"RANGE"}&_='
    res = requests.get(url, headers=head).json()
    if res['rows'] == []:
        return index,out,user
    else:
        user = res['rows'][0]['service_uid']
    for i in res['rows']:
        if i['source'] == '被动手机号' and i['tag'] == []:
            index += 1
        else:
            out += 1
    return index, out, user


def K_F(serverid, num,wbk):
    if serverid=='' or num==0:
        return
    else:
        pre=wbk['F'+str(csline)].value
        print(pre)
        price = float(pre)*int(num)
        print(price)
        ul = 'https://erp.lm12301.com/lvmeng.php/customer/customerservice/validlogadd?uid=%s&dialog=1' % serverid
        print(ul)
        data = {
        'row[id]': '',
        'row[valid_date]': today,
        'row[valid_fans]': num,
        'row[valid_price]': '0.00',
        'row[valid_total_price]': '%s' % str(price)
        }
        res=requests.post(url=ul, headers=head, data=data)
        print(res.text)


def ydata(da):
    return da[0]


def ndata(da):
    return da[1]


def ddata(da):
    return da[2]


def zb_itrm():
    wsa['D' + str(line)] = const
    for i in range(0, len(ZB)):
        reurs = a(ZB[i])
        sum = int(line) + i
        wsa['G' + str(sum)] = ydata(reurs)
        wsa['H' + str(sum)] = ndata(reurs)
    wb.save(r'C:\Users\Administrator\Desktop\2021数据\2021年广告投放加粉效果总统计.xlsx')

def ex():
    for i in range(0, len(csZB)):
        reurs = a(csZB[i])
        K_F(ddata(reurs), ydata(reurs),cswsa)
    for i in range(0, len(ZB)):
        reurs = a(ZB[i])
        K_F(ddata(reurs), ydata(reurs),wsa)
def cs_itm():
    cswsa['D' + str(csline)] = csconst
    for i in range(0, len(csZB)):
        reurs = a(csZB[i])
        sum = int(csline) + i
        cswsa['G' + str(sum)] = ydata(reurs)
        cswsa['H' + str(sum)] = ndata(reurs)
    cswb.save(r'C:\Users\Administrator\Desktop\2021数据\2021年潮汕精英广告投放加粉效果总统计.xlsx')


def execl_main():
    zb_itrm()
    cs_itm()

execl_main()
ex()
