from playground.models import *
from playground.yash_conv import *
def ifStatus(req):
      speech = "Hello"
      name = getContextData(req,"userinfo").get('name1')
      q1 = Orders.objects.get(name=name)
      q2 = Product.objects.get(item = q1.cloth).image_url
      suggestions = ["Order Again"]
      title = "For "+ name
      fulfillment_text = "you ordered "+ str(q1.quantity)+" "+ q1.color + " " + q1.cloth + " of size " + q1.size[0]
      data = basicCard(speech,title,None,fulfillment_text,q2,"CROPPED","image_text",None,None,None,suggestions,True)
      return data