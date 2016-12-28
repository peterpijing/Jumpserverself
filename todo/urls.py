from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^todolist/$', todolist, name='todo'),
    url(r'^addtodo/$', addtodo, name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', todofinish, name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$',todoback, name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', updatetodo, name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', tododelete, name='delete'),

]