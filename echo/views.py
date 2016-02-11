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


    #return render(request, "index.html", {})
    return HttpResponse()
