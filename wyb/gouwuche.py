# from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from wyb.models import product
from django.shortcuts import render
import wyb
from django.shortcuts import redirect
from django.core import paginator
from django.shortcuts import HttpResponse
class car(object):
    def __init__(self, product, count):
        self.product = product
        self.count = count
        self.sum = str((int(product.price0)) * (int(count)))
        # 属性也可以是字典
        self.pdc_dict = {}

    def resetsum(self):
        self.sum = str((int(self.product.price0)) * (int(self.count)))
    def cutcount(self):
        self.count=int(self.count)-1
    def addcount(self):
        self.count=int(self.count)+1
def reset_allsum(request,carlist):
    allsum = 0
    for list in carlist:
        allsum = allsum + int(list.sum)
    try:
        del request.session['allsum']
    except:
        print("error")
    finally:
        request.session['allsum'] = allsum
    print(request.session.get("allsum"))

def add_to_cart(request):
    number = request.GET.get("number")
    if request.session.get('username') == None:
        return render(request, 'index1.html')
    p = wyb.models.product.objects.get(number=number)
    mycar = car(p, "1")
    mycar.resetsum()
    print(mycar.sum)
    aa = request.session['car']
    flag = None
    if aa == None:
        carlist = []
        carlist.append(mycar)
        request.session['car'] = carlist
        reset_allsum(request, carlist)
    else:
        carlist = aa
        for obj in carlist:
            if mycar.product.number == obj.product.number:
                obj.count = str(int(obj.count) + 1)
                obj.resetsum()
                flag = 1
        if (flag == None):
            carlist.append(mycar)
        del request.session['car']
        reset_allsum(request,carlist)
        request.session['car'] = carlist
        print(car)
    return redirect("/car")


def carcut(request):
    if request.method == "GET":
        number = request.GET.get("number")
        carlist = request.session.get("car")
        allsum = request.session.get("allsum")
        for car in carlist:
            if car.product.number==number:
                car.cutcount()
                car.resetsum()
        reset_allsum(request,carlist)
        print(request.session.get("allsum"))
        return HttpResponse("home")

def caradd(request):
    if request.method == "GET":
        number = request.GET.get("number")
        carlist = request.session.get("car")
        allsum = request.session.get("allsum")
        for car in carlist:
            if car.product.number == number:
                car.addcount()
                car.resetsum()
        reset_allsum(request, carlist)
        print(request.session.get("allsum"))
        return HttpResponse("home")
def delete_from_car(request):
    number = request.GET.get("number")
    if request.session.get('username') == None:
        return render(request, 'index1.html')
    carlist = request.session.get("car")
    allsum = request.session.get("allsum")
    i = 0
    for car in carlist:

        if car.product.number == number:
            del carlist[i]
        i=i+1
    del request.session['car']
    request.session['car'] = carlist
    reset_allsum(request, carlist)
    return redirect("/car")

