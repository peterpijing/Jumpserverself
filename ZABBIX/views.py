# -*- coding: utf-8 -*-
from django.shortcuts import  render,render_to_response,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse #,JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required  #setting: LOGIN_URL = '/auth/login/'
from django.shortcuts import redirect
# from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm
from models import *
# from CMDB.models import *
from ZabbixAPI import ZabbixAPI
import json
from django.forms.models import model_to_dict
import re
from pyzabbix import ZabbixAPI
import ConfigParser
import datetime
import time

##TODO 1 if you want to use ---> return my_render
from django.template import RequestContext  #is it need??
from jumpserver.api import my_render, get_object, CRYPTOR

##TODO 2 locals() 会返回host_list && group_list && template_list 的值到'ZABBIX/host.html'


##1.获取host列表HostGet()
@login_required
def host(request):
    try:
        zapi=ZabbixAPI()  #instanse
        ###TODO ---now 操作之前是不是应该先登录zabbix?????

        host_list=zapi.HostGet()
        group_list=zapi.HostGroupGet()
        template_list=zapi.TemplateGet()
    except Exception as e:
        error=str(e)
    return render(request,'ZABBIX/host.html',locals())


#2.根据获取前端数据－>创建主机
@login_required
def host_create(request):
    name=request.GET.get('name','')
    ip=request.GET.get('ip','')
    groupid=request.GET.get('groupid','')
    templateid=request.GET.get('templateid','')

    try:
        zapi=ZabbixAPI()
        hostcreate=zapi.HostCreate(name,ip,groupid,templateid)
        if hostcreate['hostids']:
            result=u"主机%s创建成功，ID为%s."%(name,hostcreate['hostids'])
        else:
            result=u"主机%s创建失败."%(name)
    except Exception as e:
        result=str(e)
    return JsonResponse(result,safe=False)


@login_required
def template(request):
    return render(request, 'ZABBIX/template.html', locals())
@login_required
def item(request):
    cf = ConfigParser.ConfigParser()
    cf.read("jumpserver/config.ini")
    #获取config.in［zabbix_server］下的itemurl值
    itemurl = cf.get("zabbix_server","itemurl")

    hostid=request.GET.get('hostid','')
    try:
        zapi=ZabbixAPI()
        host_list=zapi.HostGet()
        if hostid:
            # 监控项列表
            item_list=zapi.ItemGet(hostid=hostid)
        else:
            item_list=zapi.ItemGet()
        #时间戳转化成日期格式
        for item in item_list:
            item['lastclock']= time.strftime('%Y/%m/%d %H:%M', time.localtime(float(item['lastclock'])))
    except Exception as e:
        error=str(e)
    return render(request, 'ZABBIX/item.html', locals())
@login_required
def graph(request):
    cf = ConfigParser.ConfigParser()
    cf.read("jumpserver/config.ini")
    graphurl = cf.get("zabbix_server","graphurl")

    hostid=request.GET.get('hostid','')
    try:
        zapi=ZabbixAPI()
        host_list=zapi.HostGet()
        if hostid:
            graph_list=zapi.GraphGet(hostid=hostid)
        else:
            graph_list=zapi.GraphGet()
    except Exception as e:
        error=str(e)
    return render(request, 'ZABBIX/graph.html', locals())
@login_required
def screen(request):
    return render(request, 'ZABBIX/screen.html', locals())
@login_required
def history(request):
    itemid=request.GET.get('itemid','')
    data_type=request.GET.get('data_type','0')
    print data_type
    try:
        zapi=ZabbixAPI()
        if itemid:
            value=[]
            clock=[]
            item=zapi.ItemGet(itemid=itemid)[0]
            host=zapi.HostGet(hostid=item['hostid'])[0]
            history_list=zapi.History(itemid,int(data_type))
            for history in history_list:
                value.append(float(history['value']))
                clock.append(time.strftime('%Y/%m/%d %H:%M', time.localtime(float(history['clock']))))
            print history_list
    except Exception as e:
        error=str(e)
    return render(request, 'ZABBIX/history.html', locals())

#TODO add zabbix test页面
def test(request):
    # return HttpResponse('无日志记录!')
    return render(request, 'ZABBIX/test.html', locals())