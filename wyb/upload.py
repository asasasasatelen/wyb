from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponse
import os
import json
import datetime
from wyb import excel

from wyb.models import file
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



def upload(request):
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    context = {}
    upload=None
    if request.method == 'POST':
        ret = {'status': False, 'data': None, 'error': None}
        try:
            user=request.session.get('username')
            # user="aa"
            # 定义要创建的目录
            path="/static/userupload/"+user
            print(path)
            # 调用函数
            mkdir(path)
            img = request.FILES.get('img')
            img.name=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+".xlsx"
            f = open(os.path.join(path, img.name), 'wb')
            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)
            ret['status'] = True
            ret['data'] = os.path.join(path, img.name)
        except Exception as e:
            ret['error'] = e
        finally:
            f.close()
            filename=path+"/"+img.name
            print(filename)
            excel.read_xlsx_to_mysql(request,filename)
            upload="上传成功"
            testdb = file(Uname=user,file_name=img.name,path=filename,Ftime=time_now)
            testdb.save()
            context['upload'] = upload
            print(json.dumps(ret))
            return render(request, 'sendexcel.html',context)

        upload="上传失败"
        context['upload'] = upload
    return render(request, 'sendexcel.html',context)
