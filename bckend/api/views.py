from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer



@api_view(['POST'])
def api_home(request,*args,**kwargs):
    data = request.data

    serializer=ProductSerializer(data=data)
    if serializer.is_valid():

        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400)




def api_test(request,*args,**kwargs):
    print(request.GET)
    print(request.POST)
    request_body = request.body

    print(request_body)

    data={}
    try:
        data=json.loads(request_body)
    except:
        pass
    print(data.keys())
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] =request.content_type
    return JsonResponse(data)


def api_login(request,*args,**kwargs):
    return JsonResponse({"message":"Hi there, this is django test login"})

