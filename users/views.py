import json
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from django.conf import settings
import jwt
import datetime
import pymongo

from users import utils



def login(request):
    if request.method=="POST":
        req_user = json.loads(request.body)
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient["mydb"]
        coll = mydb['users']
        # print(req_user)
        coll.insert_one({'email':req_user['email'],'password':req_user['password']})
        
        return JsonResponse({'status': True})
        
def register(request):
    if request.method=="GET":
        req_user = json.loads(request.body)
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient["mydb"]
        coll = mydb['users']
        # productList=[]
        if coll.find_one({'email':req_user['email'],'password':req_user['password']}):
            obj=coll.find_one({'email':req_user['email'],'password':req_user['password']})
            obj['_id'] = str(obj['_id'])
            return JsonResponse({'status': True, 'products': obj})
        else:
            return JsonResponse({'status': False})
        