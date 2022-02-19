
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
        'fulfillmentText':'Hello Peter'
    }

def social_login(request):
    # token = request.GET["code"]
    token = "13133131"
    return HttpResponse(token);