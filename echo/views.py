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
        
        if data['MsgType'] == 'text':
            data['Content'] = u"家政保洁欢迎您"
            data['FromUserName'], data['ToUserName'] = data['ToUserName'], data['FromUserName']
            response = utils.generate_response(data)
            #response = user_msg
            #response.find('ToUserName').text = data['FromUserName']
            #response.find('FromUserName').text = data['ToUserName']
            #response.find('Content').text = data['Content']
            #response.find('CreateTime').text = time.time()
            #to = "<ToUserName><![CDATA[%s]]></ToUserName>" % data['FromUserName']
            #server = "<FromUserName><![CDATA[%s]]></FromUserName>" % data['ToUserName']
            #respon_msg = "<Content><![CDATA[%s]]></Content>" % (data['Content'] + 'fucking asshole')
            #msg_type = "<MsgType><![CDATA[%s]]></MsgType>" % data['MsgType']
            #create_time = "<CreateTime><![CDATA[%s]]></CreateTime>" % str(int(time.time()))
            #response = '<xml>' + to + server + create_time + msg_type + respon_msg + '</xml>'

            return HttpResponse(response, content_type='text/xml')

        if data['MsgType'] == 'image':
            to = "<ToUserName><![CDATA[%s]]></ToUserName>" % data['FromUserName']
            server = "<FromUserName><![CDATA[%s]]></FromUserName>" % data['ToUserName']
            #pic_url = "<PicUrl><![CDATA[%s]]></PicUrl>" % data['PicUrl']
            msg_type = "<MsgType><![CDATA[%s]]></MsgType>" % data['MsgType']
            create_time = "<CreateTime><![CDATA[%s]]></CreateTime>" % str(int(time.time()))
            media_id = "<Image><MediaId><![CDATA[%s]]></MediaId></Image>" % data['MediaId']
            response = '<xml>' + to + server + create_time + msg_type + media_id + '</xml>'
            print response
            return HttpResponse(response, content_type="application/xml")


    #return render(request, "index.html", {})
    return HttpResponse()
