#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

news_patterns = patterns(
        'app.news.views',
        url(r'^card_add$', 'card_add', name='card_add'),
        url(r'^card_del$', 'card_del', name='card_del'),
        url(r'^card_thing$', 'card_thing', name='card_thing'),
        url(r'^comment_thing$', 'comment_thing', name='comment_thing')
)
