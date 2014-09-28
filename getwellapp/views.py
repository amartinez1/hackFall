from django.shortcuts import render
from django.views.generic import TemplateView

import requests
import json

globalUrl = 'https://api.cloud-elements.com/elements/api-v1/messaging/send'


class IndexView(TemplateView):
    template_name = 'index.html'


def twilio(to, message):
    element = "y7wrJ2ga3CZ6a0qxyQTCwLTLqrsw5FMrGSCCWS0/64w="
    data = {"message": {
            "to": "+1" + to,
            "message": message
            },
            "elementToken": element}

    headers = {'Authorization': 'Element ' + element}

    r = requests.post(globalUrl, data=json.dumps(data), headers=headers)
    return r.json()


def sendGrid(to, message):
    element = "v05S5KM3vraFACU3sj8lXM0zdKb22RSrAjbxnI2mS1Q="
    data = {"message": {
            "from": "getwell@development.com",
            "to": to,
            "subject": "Getwell tip.",
            "message": message
            },
            "elementToken": element}

    headers = {'Authorization': 'Element ' + element}

    r = requests.post(globalUrl, data=json.dumps(data), headers=headers)
    return r.json()
