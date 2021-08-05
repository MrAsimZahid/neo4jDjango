from django.http import JsonResponse
from neo4janddjango.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from neo4janddjango.forms import FriendForm
from django.shortcuts import render


@csrf_exempt
def connectPaC(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        uid = json_data['uid']
        code = json_data['code']
        try:
            person = Person.nodes.get(uid=uid)
            city = City.nodes.get(code=code)
            res = person.city.connect(city)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def connectPaP(request):
    if request.method == 'GET':
        print('hello')
        try:
            fri = FriendForm()
            # create_relation
            return render(request, "neo4janddjango/create_relation.html", {'friend_form': fri})
        except Exception as e:
            print('Exception')
            print(e)
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        print("hi")
        json_data = FriendForm(request.POST)
        if json_data.is_valid():
            print('Hi')
            uid1 = json_data.cleaned_data['f1_uid']
            uid2 = json_data.cleaned_data['f2_uid']
        # json_data = json.loads(request.body)
        # uid1 = json_data['uid1']
        # uid2 = json_data['uid2']
        try:
            person1 = Person.nodes.get(uid=uid1)
            person2 = Person.nodes.get(uid=uid2)
            res = person1.friends.connect(person2)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)