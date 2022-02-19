class ValueMissing(Exception):
	pass

class ValueNotFound(Exception):
	pass

class indexErr(Exception):
	pass

def get_parameters(req,name=None):
	if name is None:
		raise ValueMissing("name of the entity is requred")
	param=req.get("queryResult").get("parameters").get(name)
	if param is None:
		raise ValueNotFound("parameter with name {} is not found".format(name))
	return param

def getContextData(req,contextName):
    cname = req['session']+"/contexts/"+contextName
    ocontext = req['queryResult']['outputContexts']
    for i in ocontext:
        if i['name'] == cname:
            return i['parameters']

#### CAROUSEL CARD####

def carousels(title=None,speech=None,items=None,outputContexts=None):
	if len(items) < 2:
		raise indexErr("at least two items should be present")
	if items is None:
		raise ValueMissing("Items can not be empty")
	if speech is None:
		raise ValueMissing("speech can not be empty")
	temps=[]
	for i in items:
		temps.append(
			{
				"optionInfo": {
					"key": i.id,
					"synonyms": [
                    	"synonym 1",
                    	"synonym 2",
                    	"synonym 3"
                  	]
				},
				"description": i.description,
				"image": {
					"url": i.image_url,
					"accessibilityText": i.image_text
				},
				"title": i.item
			}

		)
		if i.item is None:
			raise ValueMissing("title can not be emtpy (item{})".format(i))
		if i.id is None:
			raise ValueMissing("key can not be empty ( item{})".format(i) )

	if outputContexts is None:

		return{
			"payload": {
				"google": {
					"expectUserResponse": True,
					"systemIntent": {
						"intent": "actions.intent.OPTION",
						"data": {
							"@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
							"carouselSelect": {
								"items": temps
							}
						}
					},
					"richResponse": {
						"items": [
							{
								"simpleResponse": {
									"textToSpeech": "This is a carousel example."
								}
							}
						]
					}
				}
			}
		}


	else :

		return {
		"payload":{
			"google":{
				"expectUserResponse":True,
				"richResponse":{
					"items":[
						{
							"simpleResponse":{
								"textToSpeech":speech
							}
						}
					]
				},
				"systemIntent":{
					"intent":"actions.intent.OPTION",
					"data":{
						"@type":"type.googleapis.com/google.actions.v2.OptionValueSpec",
						"carouselSelect":{
							"items":temps
						}
					}
				}
			}
		},
		"outputContexts": outputContexts ,
	}

def list_item_selectd(req):
	try:
		key=req.get("originalDetectIntentRequest").get("payload").get("inputs")[0].get('arguments')[0].get("textValue")
		return key
	except Exception as e:
		print(e)
		return False

#### BASIC CARD ####

def basicCard(speech=None,title=None,formatted_text=None,subtitle=None,card_image=None,image_scale=None,image_text=None,link_title=None,link_url=None,outputContexts=None,suggestions = None,response=True):
	if speech is None:
		raise ValueMissing("Speech can not be empty")
	# if (card_image and formatted_text is None):
	# 	raise ValueMissing("Either Formatted  text or Image Url should be used")
	if title is None:
		print("title should not be empty")

	if suggestions is None:
		raise ValueMissing("Suggestions can not be empty")

	if image_scale is None:
		image_scale="CROPPED"

	suggestionList = []
	for i in suggestions:
		suggestionList.append({"title": i})

	if outputContexts is None:

		return {
			"payload":{
				"google":{
					"expectUserResponse":response,
					"richResponse":{
						"items":[
							{
								"simpleResponse":{
									"textToSpeech":speech
								}
							},
							{
								"basicCard":{
									"title":title,
									"subtitle":subtitle,
									"formattedText":formatted_text,
									"image":{
										"url":card_image,
										"accessibilityText":image_text,
									},
									"buttons":[
										{
											"title":link_title,
											"openUrlAction":{
												"url":link_url
											}
										}
									],
									"imageDisplayOptions":image_scale
								}
							}
						],
						"suggestions": suggestionList,

					}
				}
			}
		}

	else:

		# contextList = []
		# for i in outputContexts:
		# 	if len(i) == 3:
		# 		jdata = {}
		# 		jdata['name'] = i[0]
		# 		jdata['lifespanCount'] = i[1]
		# 		jdata['parameters'] = i[2]
		# 	elif len(i) == 2:
		# 		jdata = {}
		# 		jdata['name'] = i[0]
		# 		jdata['lifespanCount'] = i[1]
		# 	else:
		# 		raise ValueMissing("lifespan and context name rquired")
		# 		contextList.append(jdata)

		return {
				"payload": {
					"google": {
						"expectUserResponse": response,
						"richResponse": {
							"items": [
								{
									"simpleResponse": {
										"textToSpeech": speech
									}
								},
								{
									"basicCard": {
										"title": title,
										"subtitle": subtitle,
										"formattedText": formatted_text,
										"image": {
											"url": card_image,
											"accessibilityText": image_text,
										},
										"buttons": [
											{
												"title": link_title,
												"openUrlAction": {
													"url": link_url
												}
											}
										],
										"imageDisplayOptions": image_scale
									}
								}
							],
							"suggestions": suggestionList,

						}
					}
				},
				"outputContexts": outputContexts,
		}

def listCard(title=None,speech=None,items=None,outputContexts = None):
	if len(items) < 1:
		raise indexErr("at least two items should be present")
	if items is None:
		raise ValueMissing("Items can not be empty")
	if speech is None:
		raise ValueMissing("speech can not be empty")
	temps=[]
	for i in items:
		temps.append(
			{
				"optionInfo":
					{
						"key":i.id,
						"synonyms":["synonym"]
					},
				"title":i.item,
				"description":i.description,
				"image":{
					"url":i.image_url,
					"accessibilityText":i.image_text
				}
			}
		)
		if i.item is None:
			raise ValueMissing("title can not be empty (item{})".format(i))
		if i.id is None:
			raise ValueMissing("key can not be empty ( item{})".format(i) )
	if outputContexts is None:
		return {
			"payload":{
				"google":{
					"expectUserResponse":True,
					"richResponse":{
						"items":[
							{
								"simpleResponse":{
									"textToSpeech":speech
								}
							}
						]
					},
					"systemIntent":{
						"intent":"actions.intent.OPTION",
						"data":{
							"@type":"type.googleapis.com/google.actions.v2.OptionValueSpec",
							"listSelect":{
								"title":title,
								"items":temps
							}
						}
					}
				}
			}
		}
	else:
		return {
			"payload": {
				"google": {
					"expectUserResponse": True,
					"richResponse": {
						"items": [
							{
								"simpleResponse": {
									"textToSpeech": speech
								}
							}
						]
					},
					"systemIntent": {
						"intent": "actions.intent.OPTION",
						"data": {
							"@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
							"listSelect": {
								"title": title,
								"items": temps
							}
						}
					}
				}
			},
			'outputContexts':outputContexts
		}

def suggestion_chips(speech=None,displayText=None,suggestions=None,outputContexts=None):

	if suggestions is None:
		raise ValueMissing("Suggestions can not be empty")
	if speech is None:
		raise ValueMissing("Speech can not be empty")
	if displayText is None:
		raise ValueMissing("displayText can not be empty")

	suggestionList=[]
	for i in suggestions:
		suggestionList.append({"title":i})

	item_list = []


	data = {
		"simpleResponse":{
		"textToSpeech":speech,
		"displayText":displayText
		}
	}
	item_list.append(data)

	if outputContexts is None:
		return  {
		"payload":{
			"google":{
				"expectUserResponse":True,
				"richResponse":{
					"items":item_list,
					"suggestions":suggestionList,
				}
			}
		}
	}

	else:

		return  {
		"payload":{
			"google":{
				"expectUserResponse":True,
				"richResponse":{
					"items":item_list,
					"suggestions":suggestionList,
				},
			}
		},
		"outputContexts": outputContexts
	}


def tablecards(speech=None):

	if speech is None:
		raise ValueMissing("speech can not be empty")

	return {
		"payload": {
			"google": {
				"expectUserResponse": True,
				"richResponse": {
					"items": [
						{
							"simpleResponse": {
								"textToSpeech": Speech

							}
						},
						{
							"tableCard": {
								"rows": [
									{
										"cells": [
											{
											"text": "row 1 item 1"
											},
											{
											"text": "row 1 item 2"
											},
											{
											"text": "row 1 item 3"
											}
										],
										"dividerAfter": True
									},
									{
										"cells": [
											{
											"text": "row 2 item 1"
											},
											{
											"text": "row 2 item 2"
											},
											{
											"text": "row 2 item 3"
											}
										],
										"dividerAfter": True
									}
								],
								"columnProperties": [
									{
										"header": "header 1"
									},
									{
										"header": "header 2"
									},
									{
										"header": "header 3"
									}
								]
							}
						},
						{
							"simpleResponse": {
								"textToSpeech": speech
							}
						}
					]
				}
			}
		}
	}