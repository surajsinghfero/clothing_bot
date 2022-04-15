import base64
import json
import logging
from constance import config
import requests

logger = logging.getLogger(__name__)


def iva_log(params=None, url=None, api_name=None, response=None):
    try:
        if api_name == "RateLIST":
            IVAResponseLog.objects.create(endpoint=response.request.url,
                                          response_code=response.status_code,
                                          method="GET",
                                          response_body=response.text,
                                          request_body=response.request.body,
                                          request_headers=response.request.headers)
            if response.status_code != 200:
                logger.debug('Unable to send to Emirates')
        elif params is None:
            IVAResponseLog.objects.create(endpoint=response.request.url,
                                          response_code=response.status_code,
                                          method="GET",
                                          response_body=response.text,
                                          request_body=response.request.body,
                                          request_headers=response.request.headers)
            if response.status_code != 200:
                logger.debug('Unable to send to Emirates')
        else:
            IVAResponseLog.objects.create(endpoint=response.request.url,
                                          response_code=response.status_code,
                                          method="POST",
                                          response_body=response.text,
                                          request_body=response.request.body,
                                          request_headers=response.request.headers)
            if response.status_code != 200:
                logger.debug('Unable to send to ADSO')
    except Exception as e:
        IVAResponseLog.objects.create(endpoint=url,
                                      response_code=500,
                                      method="POST",
                                      response_body="System Generated Message : Connection Fail at Emirates Server Side",
                                      request_body=params,
                                      request_headers={'X-Api-Key': config.SERVER_AUTH_KEY})
        logger.error(e)


def getToken(req):
    try:
        if req["originalDetectIntentRequest"]["payload"]["user"]["idToken"]:
            tkn = req["originalDetectIntentRequest"]["payload"]["user"]["idToken"]
            tkn = tkn.split('.')
            decoded_token = base64.b64decode(tkn[1] + '=' * (4 - len(tkn[1]) % 4))
            decoded_token = json.loads(decoded_token)
            return decoded_token
        else:
            return False
    except Exception as e:
        logger.debug("error in get token: {}".format(e))
        return False


def getUsertype(gmail_id):
    return 'Z'


def send_data_to_emirates(whatsapp_dict, url):
    try:
        response = requests.post(url=url, json=whatsapp_dict,
                                 headers={'X-Api-Key':'B2H3B2JH3B-3r@70ftk234DWwru=f^32J3JN#%c2ha86x&jk%'})
        WhatsappRequestResponseLog.objects.create(endpoint=response.request.url,
                                                  response_code=response.status_code,
                                                  method="POST",
                                                  response_body=response.text,
                                                  request_body=response.request.body,
                                                  request_headers=response.request.headers,
                                                  google_assistant=True)
        if response.status_code != 200:
            logger.debug('Unable to send to Emirates')
    except Exception as e:
        WhatsappRequestResponseLog.objects.create(endpoint=url,
                                                  response_code=500,
                                                  method="POST",
                                                  response_body="System Generated Message : Connection Fail at Emirates Server Side",
                                                  request_body=whatsapp_dict,
                                                  request_headers={'X-Api-Key':'B2H3B2JH3B-3r@70ftk234DWwru=f^32J3JN#%c2ha86x&jk%'},
                                                  google_assistant=True)
        logger.error(e)
