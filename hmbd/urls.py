# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include
from django.contrib import admin

from app.mmGrid.urls import grid_patterns
from app.news.urls import news_patterns
from app.urls import hmbd_patterns
from app.views import rest_api, login
from app.weight.urls import weight_patterns

admin.autodiscover()

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(hmbd_patterns)),
    path('', include(grid_patterns)),
    path('', include(weight_patterns)),
    path('', include(news_patterns)),
    path('api', rest_api),
    path('', login),
]
