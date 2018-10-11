from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255)
class user(models.Model):
    name = models.CharField( null=True,max_length=255)
    password=models.CharField(null=True,max_length=255)
    email= models.EmailField(null=True,max_length=255)
    phone = models.CharField(null=True,max_length=255)
    beizhu=models.CharField(null=True,max_length=255)
class dingdang(models.Model):
    #用户名
    Uid=models.CharField( null=True,max_length=255)
    #产品编号
    Pid=models.CharField( null=True,max_length=255)
    #购买数量
    count=models.CharField( null=True,max_length=255)
    #买家会员名
    buyname=models.CharField(null=True, max_length=255)
    #买家备注
    beizhu=models.CharField(null=True, max_length=255)
    #收货人名
    sengdforname = models.CharField(null=True, max_length=255)
   #收货地址
    address= models.CharField(null=True, max_length=255)
    #电话号码
    phone= models.CharField(null=True, max_length=255)
    #淘宝订单号
    tbID= models.CharField(null=True, max_length=255)
    #物流公司
    wuliu= models.CharField(null=True, max_length=255)
    #物流单号
    wlID=models.CharField(null=True, max_length=255)
class product(models.Model):
    #产品编号
    number = models.CharField( null=True,max_length=255)
    #产品名
    name = models.CharField( null=True,max_length=255)
    #类型
    type=models.CharField(null=True,max_length=255)
    #关键字
    key=models.CharField(null=True,max_length=255)
    #图片地址
    imgurl= models.EmailField(null=True,max_length=255)
    imgurl0= models.EmailField(null=True,max_length=255)
    imgurl1= models.EmailField(null=True,max_length=255)
    imgurl2= models.EmailField(null=True,max_length=255)
    #产品价格
    price= models.CharField(null=True,max_length=255)
    #优惠价格
    price0=models.CharField(null=True,max_length=255)
    #库存数
    count= models.CharField(null=True, max_length=255)