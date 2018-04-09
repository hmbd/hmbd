#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from app.news import views

news_patterns = [
    path('card_add', views.card_add, name='card_add'),
    path('card_del', views.card_del, name='card_del'),
    path('card_thing', views.card_thing, name='card_thing'),
    path('comment_thing', views.comment_thing, name='comment_thing')
]
