from.yash_conv import *
from django.http import HttpResponse,JsonResponse
import json
from.intents.default_welcome_intent import *
from.intents.get_cloth import *
from.intents.get_size import *
from.intents.get_color import *
from.intents.get_quantity import *
from.intents.if_confirm import *
from.intents.if_status import *
from.intents.if_order import *
def makeFulfillment(request):
    req = json.loads(request.body)
    data = ''
    intent_name = req.get('queryResult').get('intent').get('displayName')
    if intent_name == 'Default Welcome Intent':
        data = welcome_intent(req)
    if intent_name == 'Iforder':
        data = ifOrder(req)
    if intent_name == 'Getcloth':
        data = getCloth(req)
    if intent_name == 'Getsize':
        data = getSize(req)
    if intent_name == 'Getcolor':
        data = getColor(req)
    if intent_name == 'Getquantity':
        data = getQuantity(req)
    if intent_name == 'Ifconfirm':
        data = ifConfirm(req)
    if intent_name == 'Ifstatus':
        data = ifStatus(req)
    return data
