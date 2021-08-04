from django.http import JsonResponse
from neo4janddjango.models import Person
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from neo4janddjango.forms import PersonForm


def display_index(request):
    if request.method == 'GET':
        try:
            return render(request, "neo4janddjango/index.html")
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)


def getAllPersons(request):
    if request.method == 'GET':
        try:
            persons = Person.nodes.all()
            p_response = []
            for person in persons:
                obj = {
                    "uid": person.uid,
                    "name": person.name,
                    "age": person.age
                }
                p_response.append(obj)
            # response_dump = json.dumps(p_response)
            # print(p_response)
#           # print(JsonResponse(response, safe=False)) # response_dump)
            return render(request, "neo4janddjango/display_person.html", {'result': p_response})
            # return JsonResponse(response, safe=False)
        except Exception as e:
            print(e)
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)


@csrf_exempt
def personDetails(request):
    print()
    if request.method == 'GET':
        # get one person by name
        # name = request.GET.get('name', ' ')
        try:
            person = PersonForm()
            # create_relation
            return render(request, "neo4janddjango/person.html", {'person_form': person})
        except Exception as e:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one person
        json_data = PersonForm(request.POST)
        # json_data = json.loads(request.body)

        if json_data.is_valid():
            # print('Hi')
            name = json_data.cleaned_data['person_name']
            age = int(json_data.cleaned_data['person_age'])
        # name = json_data['name']
        # age = int(json_data['age'])
        try:
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
