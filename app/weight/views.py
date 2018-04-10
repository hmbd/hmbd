# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
import logging
import re
from bson import ObjectId
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from common.decorators import login_required
from common.mongo_helper import get_db
from common.utc import local2utc, utc2local


# 查询信息
def query_query(request, o_id):
    db = get_db()
    if not o_id:
        m = db.ebf_weight.find()
        u = []
        for x in m:
            # 把'_id'改为'id'
            x = {key.strip('_'): value for key, value in x.items()}
            x['system_time'] = utc2local(x['system_time']).strftime("%Y-%m-%d %H:%M:%S")
            u.append(x)
    else:
        try:
            _id = ObjectId(o_id)
            l = db.ebf_weight.find_one({'_id': _id})
            u = []
            l = {key.strip('_'): value for key, value in l.items()}
            l['system_time'] = utc2local(l['system_time']).strftime("%Y-%m-%d %H:%M:%S")
            u.append(l)
        except Exception as e:
            print('查询异常：', e)
            u = None
    return u


@login_required
def mongodb_add(request):
    if request.method == 'GET':
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return render(request, 'weight/mongodb-add.html', locals())
    elif request.method == 'POST':
        weight = request.POST.get('weight')
        run_time = request.POST.get('run_time')
        remark = request.POST.get('remark')
        if re.match(r"^[\d]*(\.{0,1})[\d]+$", weight) and re.match(r"^[\d]*(\.{0,1})[\d]+$", run_time) and not re.match(
                r"^\s*$/", remark):
            j_date_time = request.POST.get('system_time')
            # 把字符串转成datetime类型
            time = datetime.datetime.strptime(j_date_time, "%Y-%m-%d %H:%M:%S")
            system_time = local2utc(time)
            db = get_db()
            post = {
                "weight": weight,  # 体重
                "run_time": run_time,  # 跑步时长
                "system_time": system_time,  # 当前时间
                "remark": remark  # 备注
            }
            posts = db.ebf_weight
            posts.insert(post)
            return HttpResponseRedirect("/main")
        else:
            message = "数据格式错误"
            return render(request, 'weight/mongodb-add.html', locals())


# 删除
@login_required
def mongodb_delete(request):
    id = getattr(request, request.method).get("id", None)
    u = query_query(request, id)
    db = get_db()
    try:
        _id = ObjectId(u[0]['id'])
        pos = db.ebf_weight.find_one({'_id': _id})
        db.ebf_weight.remove({"_id": pos["_id"]})
        return HttpResponse(
            '<html><script type="text/javascript">alert("删除成功"); ''window.location="/mongodb_query"</script></html>')
    except Exception as e:
        print('删除异常：', e)
        return HttpResponse(
            '<html><script type="text/javascript">alert("删除失败"); ''window.location="/mongodb_query"</script></html>')


# 修改
@login_required
def mongodb_update(request):
    if request.method == 'GET':
        try:
            id = request.GET.get("id", None)
            res = query_query(request, id)
            rc = res[0]
            rc['system_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return render_to_response('weight/mongodb-update.html', {'d': rc})
        except Exception as e:
            print('修改异常：', e)
            return HttpResponse(
                '<html><script type="text/javascript">alert("修改异常"); ''window.location="/mongodb_query"</script></html>')
    elif request.method == 'POST':
        db = get_db()
        o_id = request.POST.get('id')
        try:
            _id = ObjectId(o_id)
        except Exception as e:
            print('查询异常：', e)
            return HttpResponse(
                '<html><script type="text/javascript">alert("_id错误"); ''window.location="/first"</script></html>')
        pos = db.ebf_weight.find_one({'_id': _id})
        weight = request.POST.get('weight')
        run_time = request.POST.get('run_time')
        remark = request.POST.get('remark')
        t = request.POST.get('system_time')
        # 把字符串转成datetime类型
        time = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
        system_time = local2utc(time)
        pos['weight'] = weight
        pos['run_time'] = run_time
        pos['remark'] = remark
        pos['system_time'] = system_time
        db.ebf_weight.update({"_id": pos['_id']}, pos)
        return HttpResponseRedirect('/main')


# 查询
@login_required
def mongodb_query(request):
    o_id = getattr(request, request.method).get("id", None)
    if request.method == 'GET':
        objects = query_query(request, o_id)
        if not objects:
            asd = None
    elif request.method == 'POST':
        objects = query_query(request, o_id)
    if objects:
        p = Paginator(objects, 10)  # 每页10条数据的一个分页器
        try:
            pagetype = getattr(request, request.method).get('pagetype', None)
            nowpage = int(getattr(request, request.method).get('nowpage', 1))
            if pagetype == 'pageup':
                nowpage -= 1
            elif pagetype == 'pagedown':
                nowpage += 1
        except Exception as e:
            nowpage = 1
        page = p.page(nowpage)  # 第?页
        asd = page.object_list  # 第?页的数据
    else:
        page = None
    return render_to_response('weight/mongodb-query.html', locals())


# high charts表格
@login_required
def weight_run(request):
    return render_to_response('weight-statistics.html')


# 异步获取数据
@login_required
def ajax_run(request):
    try:
        # 从mongodb数据库中获取数据
        db = get_db()
        system_time = []
        run_time = []
        weight = []
        for u in db.ebf_weight.find().sort([("system_time", -1)])[:31]:
            system_time.append(utc2local(u['system_time']).strftime("%Y-%m-%d %H:%M:%S"))
            run_time.append(float(u['run_time']))
            weight.append(float(u['weight']))
        time = json.dumps(system_time[::-1])
        number_run = json.dumps(run_time[::-1])
        number_wei = json.dumps(weight[::-1])

        if not isinstance(time, str) or not isinstance(number_run, str) or not isinstance(number_wei, str):
            time = time.decode("utf-8")
            number_run = number_run.decode("utf-8")
            number_wei = number_wei.decode("utf-8")
        name_dict = {'system_time': time, 'number_run': number_run, 'number_wei': number_wei}
        return JsonResponse(name_dict)
    except Exception as e:
        logging.error(e)
        return HttpResponse('<html><script type="text/javascript">alert("从mongodb获取数据失败"); '
                            'window.location="/main"</script></html>')
