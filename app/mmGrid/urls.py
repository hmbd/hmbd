#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from app.mmGrid import views

grid_patterns = [
    path('ad_content', views.ad_content, name='ad_content'),
    path('ad_content_edit', views.ad_content_edit, name='ad_content_edit'),
    path('ad_content_delete', views.ad_content_delete, name='ad_content_delete'),
    # \w 表示匹配大小写英文字母、数字以及下划线，等价于'[A-Za-z0-9_]'。\S 表示匹配非空白字符
    path('content_detail/<str:num_id>', views.content_detail, name='content_detail'),
]
