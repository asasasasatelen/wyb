"""wyb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wyb import view
from django.conf.urls import url
from wyb import upload
from wyb import login
from wyb import product
from wyb import testdb
from wyb import register
from wyb import outlogin
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

django.setup()
urlpatterns = [
    url(r'^$', view.index1),
    url(r'^login$', view.login),
    url(r'^register$', view.register),
    url(r'^single$', view.single),
    url(r'^product/(\d*)$', product.getproduct),
    url(r'^contact$', view.contact),
    url(r'^userhome$', view.userhome),
    url(r'^sendexcel$', view.sendexcel),
    url(r'^upload$', upload.upload),
    url(r'^loginuser$', login.login),
    url(r'^test$', view.admin),
    url(r'^uploadproduct$', product.uploadproduct),
    # url(r'^index1$', view.index1),

    url(r'^toregister$', register.register),
    url(r'^tologin$', login.login),
    url(r'^outlogin$', outlogin.outlogin),
    url(r'^admin_p$', view.admin),
    url(r'^admin_u$', view.updateP),
    url(r'^productUS$', product.getupdateP),
    url(r'^productUS1$', product.updateP),
    url(r'^admin_d$', view.productD),
    url(r'^productDS$', product.getdelectP),
    url(r'^productDS1$', product.delectP),
]
