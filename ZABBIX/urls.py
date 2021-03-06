# coding:utf-8
from django.conf.urls import patterns, include, url
from ZABBIX.views import *

urlpatterns = patterns('',
                        url(r'^host/$', host, name='host'),
                        url(r'^host_create/$', host_create, name='host_create'),
                        url(r'^item/$', item, name='item'),
                        url(r'^template/$', template, name='template'),
                        url(r'^graph/$', graph, name='graph'),
                        url(r'^history/$', history, name='history'),
                        url(r'^test/$', test, name='test'),
                      )
