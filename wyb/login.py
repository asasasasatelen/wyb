from django.shortcuts import render, redirect, reverse
from wyb.models import user
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import Context

import wyb.urls
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    email = request.POST.get('email')
    password = request.POST.get('password')
    user=getUser(email)
    if user ==None:
        context={}
        context['message']="此用户不存在"
        return render(request, 'login.html',context)
    else:
        if user.password==password:
            context = {}
            request.session['username'] = user.name
            request.session['car'] = None
            context["username"] = request.session.get('username')
            return render(request, 'index1.html',context)
        else:
            context={}
            context['message'] = "密码错误"
            return render(request, 'login.html',context)



    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     return redirect(reverse('login:home'))
    # else:
    #     return render(request, 'login.html', {
    #         'username': username,
    #         'password': password,
    #     })

def getUser(word):
    a=word

    try:
        b = user.objects.get(email=a)

    except user.DoesNotExist:
        return None
    return b
