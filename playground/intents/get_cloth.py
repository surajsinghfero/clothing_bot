from playground.yash_conv import *
from playground.models import *

def getCloth(req):
    key = int(float(list_item_selectd(req)))
    q1 = Product.objects.get(id=key)
    name = getContextData(req,"iforder").get("name1")
    cloth = q1.item
    print(cloth)
    suggestions = ['XS','S','M','L','XL']
    card_image = "https://rukminim1.flixcart.com/image/300/300/j9it30w0/measurement-tape/j/k/e/60-60-inch-heirloom-quality-original-imaez9tanxqtpfdb.jpeg?q=90"
    outputContexts = [
        {
            "name": req['session'] + "/contexts/" + "withcloth",
            "lifespanCount": 1,
            "parameters": {
                'cloth': cloth ,
                'name1': name,
            }
        }
    ]
    speech = "Please tell size"

    data = basicCard(speech,"Let's check your size" ,None,None,card_image,"CROPPED","Size-meter",None,None,outputContexts,suggestions,True)
    return data