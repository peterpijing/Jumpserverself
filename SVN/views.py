# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import os,datetime

# Create your views here.

def index(request):
    #TODO 4 调用SvnAPI
    return render(request, 'ZABBIX/test.html', locals())


######1.获取文件开头6行
# def readhead6(filename):
#     with open(filename) as f:
#         last = []
#         last1 = f.readline()[0:6]
#         for i in last1:
#           last.append(i.strip())
#         print last
#         return last


#######2.获取文件倒数6行
def readlast6(filename):
    with open(filename) as f:
        last1=[]
        last = f.readlines()[-6:]
        for i in last:
            last1.append(i.strip())
        return last1


####获取倒数6行的内容
# def lastline(f):
#     global pos
#
#     while True:
#         pos = pos - 1
#         try:
#             f.seek(pos, 2)  # 从文件末尾开始读
#             if f.read(1) == '\n':
#                 break
#         except:  # 到达文件第一行，直接读取，退出
#             f.seek(0, 0)
#             print f.readline().strip()
#             return
#
#     print f.readline().strip()





def test(request):
    # return HttpResponse('无日志记录!')
    #return render(request, 'ZABBIX/svntest.html', locals())
    # os.chdir('/opt/watchdog')
    #while True:

    # text = os.popen('sh watchdoglisten.sh').readlines()

    nownow = datetime.datetime.now()
    nownow2 = nownow.strftime('%Y%m%d')
    logging_file_name = '%s.log' % nownow2

    #1.给前端返回一个list,内容为文件前6行 python /opt/watchdog/watchdoglisten.py /usr/local/src
    content = readlast6('/opt/watchdog/logs/%s' % logging_file_name)


###TODO 读取文件最后6行
    # f = open('/opt/watchdog/logs/%s' % logging_file_name, 'rb')  # ‘r’的话会有两个\n\n
    # pos = 0
    # for line in range(6):  # 需要倒数多少行就循环多少次
    #     lastline(f)
    # f.close()


    #2.把列表换成str,并加上\n
    #content = ('\n').join(content)
    #每次访问svn/test自动刷新页面
    # last = os.popen('head -n 10 /opt/watchdog/logs/logs.log').read()

    # content = 'oko'
    # return HttpResponse(content)
    return render(request, 'ZABBIX/svntest.html', locals())