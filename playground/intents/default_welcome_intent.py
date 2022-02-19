from playground.yash_conv import *
def welcome_intent(req):
  title =  "Weclome"
  subtitle= "My name is Kiya"
  formattedText= "I'm being tested by Yash"
  card_image= "https://image.shutterstock.com/image-vector/woman-man-clothes-accessories-collection-600w-1488991403.jpg"
  image_text = "Cloth order tab"
  link_url="https://assistant.google.com/"
  link_title = "Button"
  suggestions = ['Order','Status','login']
  name = get_parameters(req, "name1")
  fulfillment_text = "Hello " + name + ", would you like to order or get current order's information?"
  outputContexts = [
    {
      "name": req['session'] + "/contexts/" + "userinfo",
      "lifespanCount": 3,
      "parameters": {
        "name1": name,
      }
    }
  ]
  data = basicCard( fulfillment_text, title, formattedText, subtitle,card_image,"CROPPED",image_text,link_title,link_url,outputContexts,suggestions,response=True)

  return data