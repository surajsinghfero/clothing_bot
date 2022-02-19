
def ask_signin(req):
    return {
        "payload": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": "PLACEHOLDER"
                            }
                        }
                    ]
                },
                "systemIntent": {
                    "intent": "actions.intent.SIGN_IN",
                    "data": {
                        "@type": "type.googleapis.com/google.actions.v2.SignInValueSpec"
                    }
                }
            }
        }
    }