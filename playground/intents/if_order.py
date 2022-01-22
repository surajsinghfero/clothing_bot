from playground.yash_conv import *
from playground.models import *
def ifOrder(req):
    speech = "Here are some options for you"
    itemset = Product.objects.all()
    name = getContextData(req,'userinfo').get('name1')
    outputContexts = [
        {
            "name": req['session'] + "/contexts/" + "iforder",
            "lifespanCount": 1,
            "parameters": {
                "name1": name,
            }
        }
    ]

    data = list(None, speech, itemset,outputContexts)
    #data = carousels(None, speech, itemset, None)
    return data