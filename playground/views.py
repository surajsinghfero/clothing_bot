from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .make_fulfillment import *


# Create your views here.
def say_hello(request):
    return HttpResponse('Hello World')


@csrf_exempt
def webhook(request):
    data = makeFulfillment(request)
    return JsonResponse(data, safe=False)


def ask_signin(request):
    return {
        'fulfillmentText': 'Hello Peter'
    }


def home(request):
    return {
        "access_token": "AYjcyMzY3ZDhiNmJkNTY",
        "refresh_token": "RjY2NjM5NzA2OWJjuE7c",
        "token_type": "Bearer",
        "expires": 3600
    }
