import pymysql
import xlrd
import datetime
from wyb.models import dingdang
def read_xlsx_to_mysql(request,filename):
    username = request.session.get('username')
    print("----------")
    excel = xlrd.open_workbook(filename)# 打开xlsx文件,返回一个对象
    sheet = excel.sheet_by_index(0)#  获取第一个sheet表格
    # # 用户名
    # Uid = models.CharField(null=True, max_length=255)
    # # 产品编号
    # Pid = models.CharField(null=True, max_length=255)
    # # 购买数量
    # count = models.CharField(null=True, max_length=255)
    # # 买家会员名
    # buyname = models.CharField(null=True, max_length=255)
    # # 买家备注
    # beizhu = models.CharField(null=True, max_length=255)
    # # 收货人名
    # sengdforname = models.CharField(null=True, max_length=255)
    # # 收货地址
    # address = models.CharField(null=True, max_length=255)
    # # 电话号码
    # phone = models.CharField(null=True, max_length=255)
    # # 淘宝订单号
    # tbID = models.CharField(null=True, max_length=255)
    # # 物流公司
    # wuliu = models.CharField(null=True, max_length=255)
    # # 物流单号
    # wlID = models.CharField(null=True, max_length=255)
    time_now = datetime.datetime.now().strftime('%Y-%m-%d:%H-%M-%S')
    for row in range(sheet.nrows):
        args = sheet.row_values(row)
        print("---新增订单--")
        print(args[0])
        if row == 0:
            print("row==0")
            testdb = dingdang(Pid=str(args[0]), count=args[1], buyname=args[2], beizhu=args[3],
                              sengdforname=args[4], address=args[5], phone=args[6], tbID=args[7], wuliu=args[8],
                              wlID=args[9],Dtime=time_now,fromfile=filename,Uid=username)
            testdb.save()
            continue
        if args[1] is None or args[1] == '':
            print("none")
            continue


if __name__ == '__main__':
    read_xlsx_to_mysql('aa.xlsx')
