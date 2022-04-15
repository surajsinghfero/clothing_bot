'''
Author: "Arjun Bhasin"
copyright: "Copyright 2019, FERO DWC LLC"
credits : ["Krunal Tank","Saif Khan"]
license: "Proprietary"
version : "0.0.1"
maintainer: "Saif Khan"
email: "saif@fero.ai"
status: "Production"
Filename: "get_signin.py"
FIle Description: "This file is for GetSignIn intent in Tia through which whole sign in functionality is done on Tia "
Date created: 05/09/2019
Date last modified: 13/11/2020
Python Version: 3.6.8 
'''

import logging
from .. import yash_conv
from ..intent_helper import getToken, getUsertype

############################
#   Intent  : Get Signin
#   Inputs  : Json requests from Dialogflow
#   Output 	: Returns Sign in info and customer tailored suggestions
############################

logger = logging.getLogger(__name__)


class SignIN:
    def signin(self, req):
        try:
            # if yash_conv.login_granted(req):
            decoded_token = getToken(req)
            gmail_id = decoded_token['email']
            logger.info("access not granted")
            sList = ['Sign In']
            res = yash_conv.suggestion_chips(
                speech=["Not Logged in, Please register on Portal first", "What else would you like to know?"],
                displayText=["Not Logged in else, Please register on Portal first",
                             "What else would you like to know?"], suggestions=sList)
            return res

        except Exception as e:
            logger.exception("get signin fulfil: {}".format(e))
            res = yash_conv.ask(speech=["Issue logging in", "What else would you like to know?"],
                           displayText=["Issue logging in", "What else would you like to know?"])
            return res
