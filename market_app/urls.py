#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 下午10:44
# @Author  : MJay_LEE
# @File    : urls.py
# @Contact : limengjiejj@hotmail.com


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^market/$', views.market, name="market"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^mine/$', views.mine, name="mine"),

    # 默认主页
    url(r'^$',views.home,name="home")
]