# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import os
import datetime
import uuid

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from PIL import Image
from common.decorators import login_required
from common.helper import qq_face_path
from common.mongo_helper import get_db
from common.mysql_helper import sql_my_profile
from common.timestamp import get_now_time_stamp


def pil_img():
    """
    pil处理图片
    :return:
    """

    # ****************png格式才可以保存***************
    # 在img被保存之前，可以进行图片的各种操作，在各种操作完成后，在进行一次写操作
    img = Image.open('图片名')
    img = img.resize((100, 100), Image.ANTIALIAS)
    # 图片名字和路径
    path = "./static/img/news/图片名"
    # 保存图片
    img.save(path)
    # **********************************************


def handle_uploaded_file(file, filename):
    if not os.path.exists('./static/img/news/'):
        os.mkdir('./static/img/news/')

    with open('./static/img/news/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


@login_required
def card_add(request):
    """
    发说说
    :param request:
    :return:
    """
    if request.method == 'GET':
        result = qq_face_path()
        return render(request, 'news/card-add.html', locals())
    elif request.method == 'POST':
        username = request.session["username"]
        result = sql_my_profile(username)
        new_content = request.POST.get("new_content", None)
        new_img = request.FILES.get('new_img', '')
        try:
            if new_img:
                handle_uploaded_file(request.FILES['new_img'], str(request.FILES['new_img']))
                new_img = "static/img/news/" + str(new_img)
            db = get_db()
            args = {
                # "new_id": str(get_now_time_stamp()) + str(uuid.uuid4()),  # 说说id
                "new_id": str(uuid.uuid4()),  # 说说id
                "username": result['username'],  # 用户名
                "nickname": result['nickname'],  # 用户昵称
                "upload_head": result['upload_head'],  # 用户头像
                "content": new_content,  # 说说内容
                "img": new_img,  # 说说图片
                "create_date": datetime.datetime.now().strftime('%Y-%m-%d %w %H:%M:%S')  # 发表时间
            }
            db.ebf_news.insert(args)
        except Exception as e:
            logging.error(e)
        return HttpResponseRedirect('/main')


@login_required
def card_del(request):
    """
    删除说说
    :param request:
    :return:
    """
    new_id = request.GET.get('new_id', '')
    if new_id:
        try:
            db = get_db()
            db.ebf_news.remove({"new_id": new_id})
            ret = {"status": 0, "data": "删除成功"}
        except Exception as e:
            logging.exception(e)
            ret = {"status": -1, "data": "删除失败"}
    else:
        ret = {"status": -1, "data": "说说id为空"}
    return HttpResponse(json.dumps(ret))


@login_required
def card_thing(request):
    """
    赞
    :param request:
    :return:
    """
    if request.method == 'POST':
        new_id = request.POST.get('new_id', '')
        user = request.POST.get('user', '')
        db = get_db()
        result = db.ebf_news.find_one({"new_id": new_id})
        if new_id and user:
            if result.get('thing'):
                thing = json.loads(result['thing'])
                if user in thing:
                    thing.remove(user)
                else:
                    thing.append(user)
            else:
                thing = []
                thing.append(user)
            db.ebf_news.update({"new_id": new_id}, {"$set": {'thing': json.dumps(thing)}})
            ret = {"status": 0, "data": "赞成功"}
        else:
            ret = {"status": -1, "data": "缺少必要参数"}
        return HttpResponse(json.dumps(ret))


@login_required
def comment_thing(request):
    """
    评论
    :param request:
    :return:
    """
    if request.method == 'POST':
        new_id = request.POST.get('new_id', '')
        now_content = request.POST.get('now_content', '')
        user = request.session.get('username')
        if new_id and now_content and user:
            db = get_db()
            result = db.ebf_news.find_one({"new_id": new_id})
            content = {
                "content_id": str(uuid.uuid4()),  # 评论id
                "new_id": new_id,  # 说说id
                "now_user": user,  # 当前评论说说的用户
                "new_user": result.get('username'),  # 发表说说的用户
                "content": now_content,  # 评论内容
                "level": 1,  # 几级评论
                "create_date": datetime.datetime.now().strftime('%Y-%m-%d %w %H:%M:%S')  # 评论时间
            }
            repeat = {
                "new_id": new_id,  # 说说id
                "now_user": user,  # 当前评论说说的用户
                "new_user": result.get('username'),  # 发表说说的用户
                "content": now_content,  # 评论内容
                "level": 1,  # 几级评论
            }
            check_repeat = db.ebf_news_content.find_one(repeat)
            if not check_repeat:
                db.ebf_news_content.insert(content)
            ret = {"status": 0, "data": "评论成功"}
        else:
            ret = {"status": -1, "data": "缺少必要参数"}
        return HttpResponse(json.dumps(ret))
