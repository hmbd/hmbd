#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http.response import HttpResponseRedirect


def login_required(func):
    """
    登录装饰器，用于判断是否登录
    :return:
    """

    def wrap(request):
        if not request.session.get('username', False):
            return HttpResponseRedirect("login")
        else:
            return func(request)

    return wrap
