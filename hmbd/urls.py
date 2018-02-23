# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from app.mmGrid.urls import grid_patterns
from app.news.urls import news_patterns
from app.urls import hmbd_patterns
from app.views import rest_api, login
from app.weight.urls import weight_patterns

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin', include(admin.site.urls)),
                       url(r'^', include(hmbd_patterns)),
                       url(r'^', include(grid_patterns)),
                       url(r'^', include(weight_patterns)),
                       url(r'^', include(news_patterns)),
                       url(r'^api', rest_api),
                       url(r'', login),
                       )
