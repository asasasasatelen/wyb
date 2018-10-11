#! /usr/bin/env python3
# coding = utf-8

import random
import pymysql


# 连接数据库函数
# def connDB(data):
#     conn = pymysql.connect(host='192.168.18.130', port=3306, user='root', passwd='123456', db='wyb', charset='utf8')  #数据库
#     cur = conn.cursor()   #游标
#     cur.execute('create table if not exists test1(id INT NOT NULL, num VARCHAR(40) );')
#     for i in range(len(data)):
#         cur.execute('insert into test1 (id,num) values("{0}","{1}");'.format(i,data[i]))   #{0} {1} 要和sql语句区分
#     cur.close()  #关游标
#     conn.commit()
#     conn.close()  #关数据库
#
#

def get_conn():
  conn = pymysql.connect(host='192.168.18.130', port=3306, user='root', passwd='123456', db='wyb', charset='utf8')
  return conn
def getproduct(word):
  conn = get_conn()
  cur = conn.cursor()
  if word=="all":
    sql = 'select * from product'
  elif word=="bianxing":
    sql='select * from product where flag="bianxing"'

  try:
    # 执行SQL语句
    cur.execute(sql)
    # 获取所有记录列表
    results = cur.fetchall()
    list = []
    listall=[]
    for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果

      list.append(fname)  ## 使用 append() 添加元素
      list.append(lname)
      list.append(age)
      list.append(sex)
      list.append(income)
      listall.append(list)
      list=[]

  except:
    print("asdas")

  # 关闭数据库连接
  conn.commit()
  cur.close()
  conn.close()
  return listall
def getid():
  conn = get_conn()
  cur = conn.cursor()
  sql='SELECT COUNT(id) FROM product'
  try:
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
      count= row[0]

  except:
      print("asdas")
  conn.commit()
  cur.close()
  conn.close()
  return count
def addproduct(name,url,introduction,money,type):
  conn = get_conn()
  cur = conn.cursor()
  id=getid()+1
  # sql = "insert into product values("+str(id)+","+name+","+url+","+introduction+","+money+","+type+")"
  sql = "INSERT INTO product VALUES (%s, %s, %s, %s, %s, %s)"
  print(sql)
  try:
    cur.execute(sql, (id,name,url,introduction,money,type))
  except:
    print("提交失败")
  conn.commit()
  cur.close()
  conn.close()
if __name__ == "__main__":
  addproduct("1","2","static/imgage/2018-10-03_16_14_54新建文本文档","4","5")
