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
        
        if data['MsgType'] == 'text':
            data['Content'] = u"一诺保洁欢迎您!"
            response = utils.generate_response(data)
            rsp_dict = {'to_user_name': data['ToUserName'],
                        'to_from_name': data['FromUserName'],
                        'create_time': time.time(),
                        'msg_type': data['MsgType'],
                        'content': data['Content']
                        }

            return render(request, "response/reply_text.xml", rsp_dict, content_type = "application/xml")

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
