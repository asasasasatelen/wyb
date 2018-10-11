from wyb.models import user
from django.http import HttpResponseRedirect
from django.shortcuts import render
def register(request):

    username = request.POST.get('name')
    password = request.POST.get('password')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    phone = request.POST.get('phone')

    if getUser(email)==None:
        saveMessage(username,password,email,phone)
        request.session['username'] = username
        context = {}
        context["username"] = request.session.get('username')
        return render(request, 'index1.html', context)

    else:
        context = {}
        context["message"] ="该邮箱已被注册"
        return render(request, 'register.html', context)

    # 初始化
def saveMessage(username,password,email,phone):
    test1 = user(name=username, password=password, email=email, phone=phone, beizhu="1")
    test1.save()
def getUser(word):
    a = word

    try:
        b = user.objects.get(email=a)

    except user.DoesNotExist:
        return None
    return b

if __name__ == '__main__':
    saveMessage('sada','dasda','asda','adasd')