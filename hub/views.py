from symbol import parameters
import requests
from django.shortcuts import render
from .models import SchemaDetails
import json
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

END_URL = {'SBI': 'http://127.0.0.1:6969/', 'BOB': 'http://127.0.0.1:3000/'}

# Create your views here.
@api_view(['POST'])
def main(request):
    bank = request.data['bank']
    action = request.data['action']
    schema_dict = SchemaDetails.objects.filter(bank = bank).values()[0]
    if (not schema_dict):
        response = {
            "status": "EmptyResponse"
        }
        return Response(response)
    print(type(schema_dict))
    #print(schema)
    schema = json.loads(schema_dict['schema'])[action]
    #print(schema)
    for key in schema:
        if key in request.data.keys():
            schema[key] = request.data[key]
        else:
            response = {
                "status": "FAILED",
                "description": "{} required but not provided!".format(key)
            }
            return Response(response)
    #schema = json.dumps(schema)
    #print(schema)
    #print(type(schema))
    r = requests.get(END_URL[bank]+action+"/", json = schema)
    return Response(r.json())

@api_view(['POST'])
def addBank(request):
    bank = request.data['bank']
    schema = "{}"
    np = SchemaDetails(bank = bank, schema = schema)
    np.save()
    return Response({"status": "OK"})

@api_view(['POST'])
def addBankFunc(request):
    bank = request.data['bank']
    action = request.data['action']
    dict = json.loads(request.data['schema'])
    item = SchemaDetails.objects.get(bank = bank)
    if (action in dict):
        response = {
            "status": "FAILED",
            "description": "Action already exists, need superuser to over write."
        }
        return Response(response)
    #print(SchemaDetails.objects)
    #print(item.schema)
    #print(dict)
    item.schema = json.dumps({ **json.loads(item.schema),   **{ action : dict}} )
    response = {
            "status": "OK",
        }
    item.save()
    return Response(response)

