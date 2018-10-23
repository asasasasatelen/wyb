from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from wyb import models
from wyb import product
from wyb.models import file
from django.core import paginator
from wyb.models import dingdang
from wyb import gouwuche
def index(request):

    return render(request, 'index.html')
def login(request):
    context = {}
    context["username"] = request.session.get('username')
    if request.session.get('username')!=None:
        return render(request, 'index1.html',context)
    return render(request, 'login.html')
def register(request):
    context = {}
    context["username"] = request.session.get('username')
    if request.session.get('username')!=None:
        return render(request, 'index1.html',context)
    return render(request, 'register.html')
def single(request):
    context          = {}
    productID=request.GET.get("product")
    print(productID)

    list=product.getsingle(productID)
    if request.session.get('username') != None:
        context['money'] = list[2]
    else:
        context['money'] = list[1]

    context['product_name'] = list[0]
    context['product_Introduction'] =list[3]
    context['imgurl'] = list[4]
    context['imgurl0'] = list[5]
    context['imgurl1'] = list[6]
    context['imgurl2'] = list[7]
    context['number'] = list[8]
    context['username']=request.session.get('username')
    return render(request, 'single.html',context)

def contact(request):
    return render(request, 'contact.html')
def userhome(request):
    context = {}
    context["username"] = request.session.get('username')
    return render(request, 'userhome.html',context)
def sendexcel(request):
    if request.session.get('username')==None:
        return render(request, 'index1.html')
    filelist=file.objects.filter(Uname=request.session.get('username'))
    context = {}
    context["username"] = request.session.get('username')
    context["filelist"] = filelist
    return render(request, 'sendexcel.html',context)

def index1(request):
    context = {}
    context["username"] = request.session.get('username')
    return render(request, 'index1.html',context)
def admin(request):
    return render(request, 'productU.html')
def updateP(request):
    return render(request, 'updateP.html')
def productD(request):
    return render(request, 'productD.html')
def car(request):
    if request.session.get('username')==None:
        return render(request, 'index1.html')
    context = {}
    username = request.session.get('username')
    context["username"]=username
    carlist = request.session.get("car")
    allsum = request.session.get("allsum")
    print("(")
    print(allsum)
    if carlist==None:
        return render(request, 'cartnone.html', context)
    else:
        context = {
            "carlist":carlist,
            "username":username,
            "allsum":allsum
        }

        return render(request, 'cart.html',context)
def pay(request):
    if request.session.get('username')==None:
        return render(request, 'index1.html')
    filepath=request.GET.get("filepath")
    # username=request.session.get('username')
    print(filepath)
    carlist=[]
    dingdanglist=dingdang.objects.filter(fromfile=filepath)
    for list in dingdanglist:
        print(list.Pid)
        p=models.product.objects.get(number=list.Pid)
        car=gouwuche.car(p,list.count)
        carlist.append(car)
    allsum = 0
    for list in carlist:
        allsum = allsum + int(list.sum)
    context = {}
    context['allsum'] = allsum
    context['carlist']=carlist
    context["username"] = request.session.get('username')
    return render(request, 'pay.html',context)