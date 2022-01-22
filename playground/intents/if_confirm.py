from playground.yash_conv import *
from playground.models import *
def ifConfirm(req):
    quantity = str(int(getContextData(req, "withquantity").get("quantity")))
    name = getContextData(req, "withquantity").get("name1")
    cloth = getContextData(req, "withquantity").get("cloth")
    size = getContextData(req, "withquantity").get("size")[0]
    color = getContextData(req, "withquantity").get("color")


    fulfillment_text = 'Dear '+  name + ', Your order for ' + quantity  + ' '+ color +' '+ cloth + '  of size ' +size+ ' is succesfull'
    user = Orders.objects.create(name=name, color=color, size=size, cloth=cloth, quantity=quantity)
    size_and_color = size + " --- " + color
    return {
		"payload": {
			"google": {
				"expectUserResponse": True,
				"richResponse": {
					"items": [
						{
							"simpleResponse": {
								"textToSpeech": fulfillment_text
							}
						},
						{
							"tableCard": {
								"rows": [
									{
										"cells": [
											{
											"text": cloth
											},
											{
											"text": size_and_color
											},
											{
											"text": quantity
											}
										],
										"dividerAfter": True
									}

								],
								"columnProperties": [
									{
										"header": "Product"
									},
									{
										"header": "Size and Color"
									},
									{
										"header": "Quantity"
									}
								]
							}
						}
					]
				}
			}
		}
	}


