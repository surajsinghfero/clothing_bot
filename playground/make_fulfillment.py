import json
from.intents import (get_signin,askSignin,default_welcome_intent,get_cloth,get_size,get_color,get_quantity,if_confirm,if_order,if_status)

get_signin = get_signin.SignIN()

intent_to_function = {
    'Default Welcome Intent': default_welcome_intent.welcome_intent,
    'LOGIN': askSignin.ask_signin,
    'Get Signin': get_signin.signin,
    'Iforder': if_order.ifOrder,
    'Getcloth': get_cloth.getCloth,
    'Getsize': get_size.getSize,
    'Getcolor': get_color.getColor,
    'Getquantity': get_quantity.getQuantity,
    'Ifconfirm': if_confirm.ifConfirm,
    'Ifstatus': if_status.ifStatus,
}

def makeFulfillment(request):
    try:
        req = json.loads(request.body)
        intent = req.get('queryResult').get('intent').get('displayName')
        print( req.get('queryResult').get('intent').get('displayName'))
        return intent_to_function.get(intent)(req)
    except Exception as e:
        return e