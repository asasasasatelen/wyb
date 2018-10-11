import pymysql
import xlrd

def get_conn():
    conn = pymysql.connect(host='192.168.18.129', port=3306, user='root', passwd='123456', db='test', charset='utf8')
    return conn
def insert(cur, sql, args):
    cur.execute(sql, args)
def read_xlsx_to_mysql(filename):
    excel = xlrd.open_workbook(filename)# 打开xlsx文件,返回一个对象
    sheet = excel.sheet_by_index(0)#  获取第一个sheet表格
    conn = get_conn()
    cur = conn.cursor()
    sql = 'insert into test values(%s,%s,%s)'
    print(sheet.nrows)
    for row in range(sheet.nrows):
        print(row)
        args = sheet.row_values(row)
        print(args)
        print(type(args))
        if row == 0:
            continue
        if args[1] is None or args[1] == '':
            continue
        insert(cur, sql, args=args)
    conn.commit()
    cur.close()
    conn.close()
if __name__ == '__main__':
    read_xlsx_to_mysql('aa.xlsx')
