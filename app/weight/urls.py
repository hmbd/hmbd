#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

weight_patterns = patterns(
        'app.weight.views',
        url(r'^mongodb_add$', 'mongodb_add', name='mongodb_add'),
        url(r'mongodb_query$', 'mongodb_query', name='mongodb_query'),
        url(r'mongodb_update$', 'mongodb_update', name='mongodb_update'),
        url(r'mongodb_delete$', 'mongodb_delete', name='mongodb_delete'),
        url(r'weight_run$', 'weight_run', name='weight_run'),
        url(r'ajax_run$', 'ajax_run', name='ajax-dict')
)
