from playground.yash_conv import *
from playground.models import *
def getColor(req):
    name = getContextData(req,"withsize").get("name1")
    cloth = getContextData(req, "withsize").get("cloth")
    size = getContextData(req, "withsize").get("size")
    key = int(float(list_item_selectd(req)))
    q1 = Color.objects.get(id=key)
    color = q1.item
    print(color)
    data = {
        'fulfillmentText': "Please tell quantity",
        'outputContexts' : [
            {
                "name": req['session'] + "/contexts/" + "withcolor",
                "lifespanCount": 1,
                "parameters": {
                    'color': color,
                    'name1': name,
                    'cloth': cloth,
                    'size': size
                }
            }
        ]

    }
    return data