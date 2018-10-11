from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from wyb import product
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
    return render(request, 'single.html',context)

def contact(request):
    return render(request, 'contact.html')
def userhome(request):
    context = {}
    context["username"] = request.session.get('username')
    return render(request, 'userhome.html',context)
def sendexcel(request):
    context = {}
    context["username"] = request.session.get('username')
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