#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json

from bson import ObjectId
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render_to_response, render

from common import code
from common.decorators import login_required
from common.helper import error, set_password, qq_face_path, font_to_img
from common.mysql_helper import sql_my_profile, sql_user_type_menu, sql_url_menu, sql_url_id, sql_menu_role
from common.mysql_helper import sql_update_menu_role, sql_update_password, sql_username_password
from common.mongo_helper import get_db, mongodb_username_card, wrap_model
from common.utc import utc2local

from model.user import User


def register(request):
    """注册
    """
    if request.method == 'POST':
        # 获得表单数据
        username = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        nickname = request.POST.get('nickname', None)
        upload_head = request.FILES['upload_head']
        if username and pwd and nickname and upload_head:
            # 判断两次密码是否一致
            if pwd != password2:
                return HttpResponse('<html><script type="text/javascript">alert("两次密码不一致"); '
                                    'window.location="/register"</script></html>')
            # 判断用户名是否已经存在
            filter_result = User.objects.filter(username=username)
            if len(filter_result) > 0:
                return HttpResponse('<html><script type="text/javascript">alert("帐号已经存在"); '
                                    'window.location="/register"</script></html>')
            pwd += username
            # 添加到数据库
            password = set_password(pwd)
            User.objects.create(username=username, password=password, nickname=nickname, upload_head=upload_head)
            return HttpResponse('<html><script type="text/javascript">alert("注册成功"); '
                                'window.location="/login"</script></html>')
        else:
            return HttpResponse('<html><script type="text/javascript">alert("数据格式不完整"); '
                                'window.location="/register"</script></html>')
    elif request.method == 'GET':
        return render(request, 'register.html')


# 登陆
def login(request):
    if request.method == 'POST':
        _code = request.POST.get('Captcha') or ''
        ca = code.Captcha()
        if ca.validate(_code):
            username = request.POST.get('username', None)
            pwd = request.POST.get('password', None)
            if username and pwd:
                pwd += username
                # 再次加密进行验证
                password = set_password(pwd)
                # 获取的表单数据与数据库进行比较
                user = User.objects.filter(username__exact=username, password__exact=password)
                if user:
                    # 比较成功，跳转index
                    response = HttpResponseRedirect('/index')
                    res = sql_my_profile(username)
                    # 将username写入浏览器session
                    request.session['username'] = username
                    # 将用户类型写入session
                    request.session['user_type'] = res['user_type']
                    # 将upload_head写入浏览器session
                    request.session['upload_head'] = res['upload_head']
                    # 将upload_head写入浏览器cookie
                    # 中文无法存入cookie中，可以存在session
                    # response.set_cookie('upload_head', upload_head)
                    # request.COOKIES['upload_head'] = upload_head
                    return response
                else:
                    # 比较失败
                    return HttpResponse('<html><script type="text/javascript">alert("帐号密码不匹配"); '
                                        'window.location="/login"</script></html>')
            else:
                return HttpResponse('<html><script type="text/javascript">alert("帐号密码不能为空"); '
                                    'window.location="/login"</script></html>')
        else:
            return HttpResponse('<html><script type="text/javascript">alert("验证码错误"); '
                                'window.location="/login"</script></html>')
    elif request.method == 'GET':
        return render(request, 'login.html')


# 登陆成功
@login_required
def index(request):
    # upload_head = request.COOKIES['upload_head']
    # upload_head = request.COOKIES.get('upload_head', '')
    username = request.session["username"]
    res = sql_my_profile(username)
    user_type = res['user_type']
    if user_type == 1:
        # 用户拥有的菜单
        menu = sql_url_id()
        all_menu = sql_url_menu()
    else:
        # 用户拥有的菜单
        menu = sql_user_type_menu(user_type)
        # 总菜单
        all_menu = sql_url_menu()
    return render(request, 'index.html', locals())


# high charts表格
@login_required
def statistics(request):
    return render(request, 'statistics.html')


# 异步获取数据
@login_required
def ajax_dict(request):
    try:
        # 缓存
        import redis

        r = redis.Redis(host='localhost', port=6379, db=0)
        h = r.dbsize()
        try:
            number = r.get('online_number')
            time = r.get('system_time')
        except:
            number = ''
            time = ''
        if not number or not time:
            # 缓存中没有数据，从mongodb数据库中获取
            db = get_db()
            system_time = []
            online_number = []
            for u in db.ebf_qq.find().sort([("system_time", -1)])[:51]:
                system_time.append(utc2local(u['system_time']).strftime("%Y-%m-%d %H:%M:%S"))
                online_number.append(int(u['online_number']))
            system_time = system_time[::-1]
            online_number = online_number[::-1]
            time = json.dumps(system_time)
            number = json.dumps(online_number)
            r.set('online_number', number)
            r.set('system_time', time)
            # 缓存中数据30秒过期
            r.expire('online_number', 30)
            r.expire('system_time', 30)
        if not isinstance(time, str) or not isinstance(number, str):
            time = time.decode("utf-8")
            number = number.decode("utf-8")
        name_dict = {'system_time': time, 'online_number': number}
        return JsonResponse(name_dict)
    except Exception as e:
        logging.getLogger('').info("读取缓存出错：" + str(e))
        return HttpResponse('<html><script type="text/javascript">alert("redis服务未开启"); '
                            'window.location="/main"</script></html>')


# 退出
@login_required
def logout(request):
    response = HttpResponseRedirect('/login')
    # 清理session里保存的username,upload_head
    del request.session['username']
    del request.session['upload_head']
    # 清理cookie里保存的upload_head
    # del request.COOKIES['upload_head']
    # response.delete_cookie('upload_head')
    return response


# 验证码
def get_code(request):
    # 单词存在word_code.list中
    ca = code.Captcha(img_width=150, img_height=30, code_type="word")
    return ca.display()


# rest
def rest_api(request):
    # 查询数据
    if request.method == "GET":
        _id = request.GET.get("_id", None)
        if _id:
            db = get_db()
            _id = ObjectId(_id)
            m = db.ebf_qq.find_one({'_id': _id})
            if m is None:
                data = {'data': 'QUERY Fail!'}
            else:
                data = {"online_number": m["online_number"], 'system_time': m["system_time"]}
            return JsonResponse(data)
        return JsonResponse({"data": "data is null"})
    # 插入数据
    elif request.method == "POST":
        online_number = request.GET.get("online_number", None)
        system_time = request.GET.get("system_time", None)
        db = get_db()
        post = {
            "online_number": online_number,
            "system_time": system_time
        }
        posts = db.ebf_qq
        posts.insert(post)
        data = {'data': 'Insert Success!'}
        return JsonResponse(data)
    # 修改数据
    elif request.method == "PUT":
        _id = request.GET.get("_id", None)
        if _id:
            online_number = request.GET.get("online_number", None)
            system_time = request.GET.get("system_time", None)
            db = get_db()
            _id = ObjectId(_id)
            pos = db.ebf_qq.find_one({'_id': _id})
            if pos is None:
                data = {'data': 'Update Fail!'}
            else:
                pos['online_number'] = online_number
                pos['system_time'] = system_time
                db.ebf_qq.update({"_id": pos['_id']}, pos)
                data = {'data': 'Update Success!'}
            return JsonResponse(data)
    # 删除数据
    elif request.method == "DELETE":
        _id = request.GET.get("_id", None)
        if _id:
            db = get_db()
            _id = ObjectId(_id)
            pos = db.ebf_qq.find_one({'_id': _id})
            if pos is None:
                data = {'data': 'DELETE Fail!'}
            else:
                db.ebf_qq.remove({"_id": pos["_id"]})
                data = {'data': 'DELETE Success!'}
            return JsonResponse(data)
    # 其他情况
    else:
        data = {'data': 'There is no corresponding operation'}
        return JsonResponse(data)


# 登陆后主页
@login_required
def main(request):
    """
    说说列表
    :param request:
    :return:
    """
    username = request.session["username"]
    content = mongodb_username_card()
    new_id_content = []
    content_id_content = []
    week = {
        '1': '周一',
        '2': '周二',
        '3': '周三',
        '4': '周四',
        '5': '周五',
        '6': '周六',
        '0': '周日',
    }
    db = get_db()
    for i in content:
        i.pop('_id')
        item = i.get('content', '')
        time = i.get('create_date', '')
        if i.get('thing'):
            i['thing'] = json.loads(i['thing'])
        if time:
            before = time[:10]
            now = time[11]
            up = week[now]
            after = time[-8:]
            i['create_date'] = before + '/' + up + '/' + after
        item = font_to_img(item)
        temp = dict()
        temp['new_id'] = i.get('new_id')
        temp['content'] = item
        new_id_content.append(temp)
        thing_content = db.ebf_news_content.find({"new_id": i.get('new_id')}).sort('create_date', -1)
        thing_content = wrap_model(thing_content)
        for k in thing_content:
            k.pop('_id')
            k['content'] = font_to_img(k.get('content'))
            info = dict()
            info['content_id'] = k.get('content_id')
            info['content'] = font_to_img(k.get('content'))
            content_id_content.append(info)
        i['thing_content'] = thing_content
    result = qq_face_path()
    return render(request, 'news/card.html', locals())


# 修改密码
@login_required
def modify_pwd(request):
    if request.method == 'POST':
        old_pwd = request.POST.get("old_pwd", None)
        new_pwd = request.POST.get("new_pwd", None)
        new_again_pwd = request.POST.get("new_again_pwd", None)
        if old_pwd and new_pwd and new_again_pwd:
            if new_pwd == new_again_pwd:
                # 从数据库获取密码
                username = request.session["username"]
                password = sql_username_password(username)
                old_pwd += username
                # 加密进行验证
                old_pwd = set_password(old_pwd)
                if password == old_pwd:
                    new_pwd += username
                    new_pwd = set_password(new_pwd)
                    result = sql_update_password(new_pwd, username)
                    if result == 'ok':
                        ret = error(0)
                else:
                    ret = error(2)
            else:
                ret = error(1)
        else:
            ret = error(3)
        return HttpResponse(ret)
    elif request.method == 'GET':
        return render(request, 'modify-pwd.html')


# 个人资料
@login_required
def my_profile(request):
    if request.method == 'GET':
        username = request.session["username"]
        result = sql_my_profile(username)
        return render(request, 'my-profile.html', locals())


@login_required
def index1(request):
    return render(request, 'extend/index1.html', locals())


# 测试1
@login_required
def test1(request):
    return render(request, 'extend/test1.html', locals())


# 测试2
def test2(request):
    return render(request, 'extend/test2.html', locals())


def top_height(request):
    return render(request, 'top-height.html', locals())


# 测试3
@login_required
def test3(request):
    # render_to_response不能加上request参数
    # render必须要加上request参数
    return render_to_response('extend/test3.html', locals())


# 二维码
def jquery_qr_code(request):
    return render(request, 'jquery-qrcode.html')


# 省市区
def province(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'code': 0, 'data': 1}))
    elif request.method == "GET":
        return render(request, 'test/province.html')


# 定位当前地址
def address(request):
    return render(request, 'test/address.html')


# css实现loading
def loading(request):
    return render(request, 'loading.html')


# 菜单
@login_required
def menu(request):
    menu_role = sql_menu_role()
    user_type = menu_role[0]['id']
    # 用户拥有的菜单
    menu = sql_user_type_menu(user_type)
    # 总菜单
    all_menu = sql_url_menu()
    if request.method == 'POST':
        asd = request.POST.get('asd', None)
        action = request.POST.get('type', None)
        user_type = request.POST.get('user_type', None)
        if user_type:
            user_type = int(user_type)
        else:
            ret = error(4)
            return HttpResponse(ret)
        # 修改操作
        if action == 'ask':
            result = sql_update_menu_role(user_type, asd)
            if result == 'ok':
                ret = error(0)
            else:
                ret = error(4)
        else:
            # 用户拥有的菜单
            menu = sql_user_type_menu(user_type)
            ret = error(0, menu)
        return HttpResponse(ret)
    return render(request, 'menu.html', locals())
