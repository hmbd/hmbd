#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

hmbd_patterns = [
        path('', views.login, name='login'),
        path('login', views.login, name='login'),
        path('register', views.register, name='register'),
        path('index', views.index, name='index'),
        path('index/index', views.index1, name='index1'),
        path('logout', views.logout, name='logout'),
        path('statistics', views.statistics, name='statistics'),
        path('ajax_dict', views.ajax_dict, name='ajax-dict'),
        path('main', views.main, name='main'),
        path('modify_pwd', views.modify_pwd, name='modify_pwd'),
        path('my_profile', views.my_profile, name='my_profile'),
        path('get_code', views.get_code, name='get_code'),
        path('test1', views.test1, name='test1'),
        path('test2', views.test2, name='test2'),
        path('test3', views.test3, name='test3'),
        path('top_height', views.top_height, name='top_height'),
        path('jquery_qr_code', views.jquery_qr_code, name='jquery_qr_code'),
        path('province', views.province, name='province'),
        path('address', views.address, name='address'),
        path('loading', views.loading, name='loading'),
        path('menu', views.menu, name='menu')
]
