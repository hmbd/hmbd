#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from app.weight import views

weight_patterns = [
    path('mongodb_add', views.mongodb_add, name='mongodb_add'),
    path('mongodb_query', views.mongodb_query, name='mongodb_query'),
    path('mongodb_update', views.mongodb_update, name='mongodb_update'),
    path('mongodb_delete', views.mongodb_delete, name='mongodb_delete'),
    path('weight_run', views.weight_run, name='weight_run'),
    path('ajax_run', views.ajax_run, name='ajax-dict')
]
