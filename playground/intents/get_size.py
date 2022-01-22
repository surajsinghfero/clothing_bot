from playground.yash_conv import *
from playground.models import *
def getSize(req):
    name = getContextData(req,"withcloth").get("name1")
    cloth = getContextData(req, "withcloth").get("cloth")
    size = get_parameters(req,"size")
    title = "Please tell color"
    itemset = Color.objects.all()
    outputContexts = [
        {
            "name": req['session'] + "/contexts/" + "withsize",
            "lifespanCount": 1,
            "parameters": {
                'cloth': cloth,
                'name1': name,
                'size': size
            }
        }
    ]
    data = carousels(title,title,itemset,outputContexts)
    return data