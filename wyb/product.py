from django.shortcuts import render
import os
import datetime
from wyb import mysql
from wyb.models import product
from django.core import paginator
import wyb.models

def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print
        path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False


def getproduct(request, index):
    context = {}
    # list = [['1','/static/images/pic13.jpg', 'a', 'aa', '100'], ['2','/static/images/pic13.jpg', 'b', 'bb', '200'], ['3','/static/images/pic13.jpg', 'b', 'bb', '200'], ['4','/static/images/pic13.jpg', 'b', 'bb', '200'], ['5','/static/images/pic13.jpg', 'b', 'bb', '200'], ['6','/static/images/pic13.jpg', 'b', 'bb', '200'], ['7','/static/images/pic13.jpg', 'b', 'bb', '200'], ['8','/static/images/pic13.jpg', 'b', 'bb', '200']]
    list = []
    username = request.session.get('username')
    aa = getalllist()
    print(request.session.get('username'))

    for a in aa:
        list2 = []
        list2.append(a.name)
        list2.append(a.key)
        list2.append(a.imgurl)
        if request.session.get('username') != None:
            list2.append(a.price)
        else:
            list2.append(a.price0)
        list2.append(a.id)
        list.append(list2)
    print(username)
    print(list2)
    count = len(list)

    pag = paginator.Paginator(list, 6)
    if index == '':
        index = 1
        # 返回指定（index）页的数据，用于呈现在指定页上
    page = pag.page(index)
    # 构造上下文，以便html文件中能调用对应页的数据
    context = {
        'page': page,
        'count': count,
        "username": username
    }
    return render(request, 'product.html', context)


def getalllist():
    try:
        p = product.objects.all()

    except product.DoesNotExist:
        return None
    return p


def getCode(word):
    a = word
    try:
        b = product.objects.get(number=a)
    except product.DoesNotExist:
        return None
    return b


def getmessage(request, time_now):
    if request.method == 'POST':
        name = request.POST.get('name')
        introduction = request.POST.get('introduction')
        money = request.POST.get('money')
        money0 = request.POST.get('money0')
        type = request.POST.get('type')
        img = request.FILES.get('img')
        img0 = request.FILES.get('img0')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        url = "/static/images/" + time_now + "_1.png"
        url0 = "/static/images/" + time_now + "_2.png"
        url1 = "/static/images/" + time_now + "_3.png"
        url2 = "/static/images/" + time_now + "_4.png"
        count = request.POST.get('count')
        number = request.POST.get('number')
        print(number)
        print(getCode(number))
        if getCode(number) == None:
            return name, url, url0, url1, url2, introduction, money, money0, type, count, number
        else:
            return None


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print
        path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False


def upload(request, time_now):
    context = {}
    upload = None
    if request.method == 'POST':
        ret = {'status': False, 'data': None, 'error': None}
        try:
            # 定义要创建的目录
            path = "static/images"
            # 调用函数
            mkdir(path)
            img = request.FILES.get('img')
            img0 = request.FILES.get('img0')
            img1 = request.FILES.get('img1')
            img2 = request.FILES.get('img2')
            img.name = time_now + "_1.png"
            img0.name = time_now + "_2.png"
            img1.name = time_now + "_3.png"
            img2.name = time_now + "_4.png"
            f = open(os.path.join(path, img.name), 'wb')
            f0 = open(os.path.join(path, img0.name), 'wb')
            f1 = open(os.path.join(path, img1.name), 'wb')
            f2 = open(os.path.join(path, img2.name), 'wb')
            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)
            for chunk in img0.chunks(chunk_size=1024):
                f0.write(chunk)
            for chunk in img1.chunks(chunk_size=1024):
                f1.write(chunk)
            for chunk in img2.chunks(chunk_size=1024):
                f2.write(chunk)
            ret['status'] = True
            ret['data'] = os.path.join(path, img.name)
        except Exception as e:
            ret['error'] = e
        finally:
            f.close()
            upload = "提交成功"

            return upload

    upload = "提交失败"

    return upload


def uploadproduct(request):
    time_now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    context = {}
    list = getmessage(request, time_now)
    context['upload'] = upload(request, time_now)
    print(list)
    print("-----------------")
    if list == None:
        context = {}
        context["message"] = "此产品已存在"
        return render(request, 'productU.html', context)
    else:
        test1 = product(name=list[0], imgurl=list[1], imgurl0=list[2], imgurl1=list[3], imgurl2=list[4], key=list[5],
                        price=list[6], price0=list[7], type=list[8], count=list[9], number=list[10])
        #
        test1.save()
        # mysql.
        return render(request, 'productU.html', context)


# 获取需更新的商品信息
def getupdateP(request):
    if request.method == 'POST':
        number = request.POST.get('code')
        p = product.objects.get(number=number)
        context = {
            'name': p.name,
            'introduction': p.key,
            'money': p.price,
            'money0': p.price0,
            'type': p.type,
            'img': p.imgurl,
            'img0': p.imgurl0,
            'img1': p.imgurl1,
            'img2': p.imgurl2,
            'count': p.count,
            'number': p.number

        }
        return render(request, 'updateP.html', context)


# 对更新的商品进行校验，若有更新进行更新
def updateP(request):
    time_now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    if request.method == 'POST':
        name = request.POST.get('name')
        introduction = request.POST.get('introduction')
        money = request.POST.get('money')
        money0 = request.POST.get('money0')
        type = request.POST.get('type')
        img = request.FILES.get('img')
        img0 = request.FILES.get('img0')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')

        url = "/static/images/" + time_now + "_1.png"
        url0 = "/static/images/" + time_now + "_2.png"
        url1 = "/static/images/" + time_now + "_3.png"
        url2 = "/static/images/" + time_now + "_4.png"
        count = request.POST.get('count')
        number = request.POST.get('number')
        print(name, introduction, money0, money, type, img, img0, img1, img2, count, number)
        p = product.objects.get(number=number)
        if name != p.name:
            p.name = name
            p.save()
        if introduction != p.key:
            p.key = introduction
            p.save()
        if money != p.price:
            p.price = money
            p.save()
        if money0 != p.price0:
            p.price0 = money0
            p.save()
        if type != p.type:
            p.type = type
            p.save()
        path = "static/images"
        if img != None:
            img.name = time_now + "_1.png"
            try:
                f = open(os.path.join(path, img.name), 'wb')
                for chunk in img.chunks(chunk_size=1024):
                    f.write(chunk)
                p.imgurl = url
                p.save()
            except Exception as e:
                print("a")
            finally:
                f.close()

        if img0 != None:

            img0.name = time_now + "_2.png"

            try:
                f = open(os.path.join(path, img0.name), 'wb')
                for chunk in img0.chunks(chunk_size=1024):
                    f.write(chunk)
                p.imgurl0 = url0
                p.save()
            except Exception as e:
                print("a")
            finally:
                f.close()
            if img1 != None:
                img1.name = time_now + "_3.png"
                try:
                    f = open(os.path.join(path, img1.name), 'wb')
                    for chunk in img1.chunks(chunk_size=1024):
                        f.write(chunk)
                    p.imgurl1 = url1
                    p.save()
                except Exception as e:
                    print("a")
                finally:
                    f.close()
            if img2 != None:

                img2.name = time_now + "_4.png"
                try:
                    f = open(os.path.join(path, img2.name), 'wb')
                    for chunk in img2.chunks(chunk_size=1024):
                        f.write(chunk)
                    p.imgurl2 = url2
                    p.save()
                except Exception as e:
                    print("a")
                finally:
                    f.close()
            if count != p.count:
                p.count = count
                p.save()
        context = {'message': "修改成功"}
        return render(request, 'updateP.html', context)

#获取删除产品的信息
def getdelectP(request):
    if request.method == 'POST':
        number = request.POST.get('code')
        p = product.objects.get(number=number)
        context = {
            'name': p.name,
            'introduction': p.key,
            'money': p.price,
            'money0': p.price0,
            'type': p.type,
            'img': p.imgurl,
            'img0': p.imgurl0,
            'img1': p.imgurl1,
            'img2': p.imgurl2,
            'count': p.count,
            'number': p.number

        }
        return render(request, 'productD.html', context)
#删除产品
def delectP(request):
    if request.method == 'POST':
        number = request.POST.get('code')
        print(number)
        product.objects.filter(number=number).delete()
        context = {
        'message':"删除成功"
    }
    return render(request, 'productD.html', context)

# 获取单个商品信息
def getsingle(word):
    id = str(word)
    p = product.objects.get(id=id)
    return p.name, p.price, p.price0, p.key, p.imgurl, p.imgurl0, p.imgurl1, p.imgurl2
