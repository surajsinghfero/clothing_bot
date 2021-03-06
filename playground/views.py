from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .make_fulfillment import *

import requests
from urllib.parse import urlencode
import json
from subprocess import Popen


# Create your views here.
@csrf_exempt
def say_hello(request):
    return HttpResponse('Hello World')


@csrf_exempt
def webhook(request):
    data = makeFulfillment(request)
    return JsonResponse(data, safe=False)


@csrf_exempt
def ask_signin(request):
    return {
        'fulfillmentText': 'Hello Peter'
    }


import string
import random

client_id = "854818672261-fupq7ursgurp18n9neqcl3t0043jhkai.apps.googleusercontent.com"
client_secret = "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"
redirect_uri = "https://oauth-redirect.googleusercontent.com/r/clothing-bbcq"
base_url = "https://accounts.google.com/o/oauth2/"
authorization_code = ""
access_token = ""

"""
Retrieving authorization_code from authorization API.
"""


@csrf_exempt
def retrieve_authorization_code():
    authorization_code_req = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": ("https://www.googleapis.com/auth/userinfo.profile" +
                  " https://www.googleapis.com/auth/userinfo.email" +
                  " https://www.googleapis.com/auth/calendar")
    }

    r = requests.get(base_url + "auth?%s" % urlencode(authorization_code_req),
                     allow_redirects=False)
    url = r.headers.get('location')
    # authorization_code = input("Authorization Code >>> ")
    authorization_code = 'MzI0MjM0MjM0MjNmc2Rmc2Rmc2RmdzM0MzJmZGVydDM0NTZ0eXJ0'
    return authorization_code


"""
Retrieving access_token and refresh_token from Token API.
"""


@csrf_exempt
def retrieve_tokens(authorization_code):
    access_token_req = {
        "code": authorization_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }
    content_length = len(urlencode(access_token_req))
    access_token_req['content-length'] = str(content_length)
    r = requests.post(base_url + "token", data=access_token_req)
    data = json.loads(r.text)
    return data
