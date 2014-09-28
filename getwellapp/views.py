from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
import httplib
import requests
import json

globalUrl = 'https://api.cloud-elements.com/elements/api-v1/messaging/send'


class IndexView(TemplateView):
    template_name = 'index.html'
 
 
def twilio(request):
    to = request.GET['to']
    message = request.GET['message']
 
    if message:
        element = "y7wrJ2ga3CZ6a0qxyQTCwLTLqrsw5FMrGSCCWS0/64w="
        data = {"message": {
                "to": "+1" + to,
                "message": message
                },
                "elementToken": element}
 
        headers = {'Authorization': 'Element ' + element}
 
        r = requests.post(globalUrl, data=json.dumps(data), headers=headers)
    return HttpResponse()

def sendGrid(request):
    to = request.GET['to']
    message = request.GET['message']
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
    return  HttpResponse()




def getCoordinates(request):
    if request.GET:
        connection = httplib.HTTPConnection('intrinsecus.crypticocorp.com', 80)
        connection.connect()
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']
        connection.request('GET', 'http://intrinsecus.crypticocorp.com/api/namespaces/ads/sources/hospitales/data/?geometry__intersects=Point(['+longitude+','+latitude+']).buffer(0.08)&_format=json', '', {})
        result = json.loads(connection.getresponse().read())
        return HttpResponse(json.dumps(result), content_type='application/json')
    return HttpResponse('')