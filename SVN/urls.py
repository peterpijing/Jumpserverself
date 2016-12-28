# coding:utf-8
from django.conf.urls import patterns, include, url
from SVN.views import *

urlpatterns = patterns('',
                        url(r'^index/$', index, name='svnindex'),
                        url(r'^test/$', test, name='svntest'),
                      )
