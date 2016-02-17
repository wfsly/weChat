#coding:utf-8
import hashlib
import time
from xml.etree import ElementTree as ET

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import utils


# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        xml = request.body
        print xml

        data = utils.parse_xml(xml)
        utils.exchange_src_des(data)
        
        if data['MsgType'] == 'event':
            if data['Event'] == 'subscribe':
                response = generate_subscribe_response(data)
            return HttpResponse(response, content_type="application/xml")

        elif data['MsgType'] == 'text':
            content = data['Content']
            if content == u'价格':
                data['Content'] = u'每平方米5元'
            if content == u'介绍':
                data['Content'] = u'这里是简介'
                rsp_dict = {'to_user_name': data['ToUserName'],
                            'to_from_name': data['FromUserName'],
                            'create_time': time.time(),
                            'msg_type': 'news',
                            'article_count': 1,
                            'title1': 'title',
                            'description1': 'description',
                            'pic_url': 'http://mmbiz.qpic.cn/mmbiz/50Rsp4bm4ickDPcw0lJnMnaZOib1zssoNSB1VGUPyicUk4JkrWeNgshfrbIPJ5py4DuZNGhctEiblohQgyU6fPictAw/0',
                            'url': ''
                        }
                return render(request, "response/reply_with_news.xml", rsp_dict, content_type = "application/xml")
            #data['Content'] = u"一诺保洁欢迎您"
            rsp_dict = {'to_user_name': data['ToUserName'],
                        'to_from_name': data['FromUserName'],
                        'create_time': time.time(),
                        'msg_type': data['MsgType'],
                        'content': data['Content']
                        }

            return render(request, "response/reply_text.xml", rsp_dict, content_type = "application/xml")
            


        elif data['MsgType'] == 'image':
            rsp_dict = {'to_user_name': data['ToUserName'],
                        'to_from_name': data['FromUserName'],
                        'create_time': time.time(),
                        'msg_type': data['MsgType'],
                        'media_id': data['MediaId']
                        }
            return render(request, "response/reply_image.xml", rsp_dict, content_type = "application/xml")

        elif data['MsgType'] == 'link':
            response = """ <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName> 
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[%s]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>""" % (data['ToUserName'], data['FromUserName'], str(int(time.time())), 'text', u"这是一个链接" + data['Title'])
            return HttpResponse(response, content_type="application/xml")


    #return HttpResponse()
def generate_subscribe_response(data):
    response = """ <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName> 
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[%s]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>""" % (data['ToUserName'], data['FromUserName'], str(int(time.time())), 'text', u"一诺保洁，真诚服务\n业务详情请咨询马女士：15552901208")
    return response 
