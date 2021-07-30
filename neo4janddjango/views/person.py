from django.http import JsonResponse
from neo4janddjango.models import Person
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.core.mail import send_mail
from neo4janddjango.forms import PersonForm


def getAllPersons(request):
    if request.method == 'GET':
        try:
            persons = Person.nodes.all()
            response = []
            for person in persons:
                obj = {
                    "uid": person.uid,
                    "name": person.name,
                    "age": person.age,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)


@csrf_exempt
def personDetails(request):
    print()
    if request.method == 'GET':
        # get one person by name
        name = request.GET.get('name', ' ')
        try:
            person = PersonForm()
            return render(request, "index.html", {'form': person})
        except Exception as e:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one person
        json_data = PersonForm(request.POST)
        # json_data = json.loads(request.body)

        if json_data.is_valid():
            print('Hi')
            name = json_data.cleaned_data['person_name']
            age = int(json_data.cleaned_data['person_age'])
        # name = json_data['name']
        # age = int(json_data['age'])
        try:
            print(name)
            print(age)
            person = Person(name=name, age=age)
            person.save()
            response = {

            }
            return JsonResponse(response)
        except Exception as e:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one person
        json_data = json.loads(request.body)
        name = json_data['name']
        age = int(json_data['age'])
        uid = json_data['uid']
        try:
            person = Person.nodes.get(uid=uid)
            person.name = name
            person.age = age
            person.save()
            response = {
                "uid": person.uid,
                "name": person.name,
                "age": person.age,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one person
        json_data = json.loads(request.body)
        uid = json_data['uid']
        try:
            person = Person.nodes.get(uid=uid)
            person.delete()
            response = {"success": "Person deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
