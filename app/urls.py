#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from app import views

hmbd_patterns = patterns(
        'app.views',
        url(r'^$', 'login', name='login'),
        url(r'login$', 'login', name='login'),
        url(r'^register$', 'register', name='register'),
        url(r'^index$', 'index', name='index'),
        url(r'^index/index$', 'index1', name='index1'),
        url(r'^logout$', 'logout', name='logout'),
        url(r'^statistics$', 'statistics', name='statistics'),
        url(r'^ajax_dict$', 'ajax_dict', name='ajax-dict'),
        url(r'^main$', 'main', name='main'),
        url(r'^modify_pwd$', 'modify_pwd', name='modify_pwd'),
        url(r'^my_profile$', 'my_profile', name='my_profile'),
        url(r'^get_code$', views.get_code, name='get_code'),
        url(r'^test1$', 'test1', name='test1'),
        url(r'^test2$', 'test2', name='test2'),
        url(r'^test3$', 'test3', name='test3'),
        url(r'^top_height$', 'top_height', name='top_height'),
        url(r'^jquery_qr_code$', 'jquery_qr_code', name='jquery_qr_code'),
        url(r'^province$', 'province', name='province'),
        url(r'^address$', 'address', name='address'),
        url(r'^loading$', 'loading', name='loading'),
        url(r'^menu$', 'menu', name='menu')
)
