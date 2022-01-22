from playground.yash_conv import *

def getQuantity(req):
    quantity = get_parameters(req, "quantity")
    name = getContextData(req, "withcolor").get("name1")
    cloth = getContextData(req, "withcolor").get("cloth")
    size = getContextData(req, "withcolor").get("size")
    color = getContextData(req, "withcolor").get("color")
    data = {
        'fulfillmentText':"Should i confirm this order?",
        'outputContexts': [
            {
                "name": req['session'] + "/contexts/" + "withquantity",
                "lifespanCount": 1,
                "parameters": {
                    'color': color,
                    'name1': name,
                    'cloth': cloth,
                    'size': size,
                    'quantity': quantity
                }
            }
        ]
    }
    return data