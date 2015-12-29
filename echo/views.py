import hashlib

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        print 'signature ' + signature

        token = 'wx192'
        args = [token, timestamp, nonce]
        args.sort()
        encrypt_signature = hashlib.sha1(args[0] + args[1] + args[2]).hexdigest()
        print 'Signature ' + encrypt_signature

        if signature == encrypt_signature:
            print echostr
            return HttpResponse(echostr)
