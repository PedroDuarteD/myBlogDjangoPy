from django.shortcuts import render, HttpResponse
from .models import Thought, User
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

# Create your views here.

# Create your views here.
def home(request):
    #depois basta ir nas urls.py
    #return HttpResponse('Django with python')
    return render(request, "my.html")

@csrf_exempt 
def setUser(request):
    data = json.loads(request.body)
    
    User.objects.create(
        name= data.get("name"),
        password= data.get("password"),
        active= 1,
    )

    return JsonResponse({"response": "Success"},safe=False)

@csrf_exempt 
def setThought(request):
    data = json.loads(request.body)
    
  


    u =User.objects.get(id=data.get("user"))

    if u.password=="":
        date =datetime.datetime.now()
        d = str(date).split(".")[0]
        publish =  d[:-3]
        
        Thought.objects.create(
        message= data.get("name"),
        user= u,
        edited= 0,
        public= 1,
        like=0,
        publish= publish,
        )
        return JsonResponse({"response": "Success"},safe=False) 
    else:

        if u.password == data.get("password"):

            date =datetime.datetime.now()
            d = str(date).split(".")[0]
            publish =  d[:-3]
            
            Thought.objects.create(
            message= data.get("name"),
            user= u,
            edited= 0,
            public= 1,
            like=0,
            publish= publish,
            )
            return JsonResponse({"response": "Success"},safe=False)    
        else:
            return JsonResponse({"response": "Error","sms" : "Pasword failed"},safe=False)    



def getUsers(request): 
    allUsersModel = User.objects.all()
    allUsers = []

    for user in allUsersModel:

        password = False
        if user.password!="":
            password = True

        allUsers.append({
            "id" : user.id,
            "name" : user.name,
            "password" : password,
        })
    return JsonResponse(allUsers, safe= False)

def thoughts(request):
    myThoughts = Thought.objects.all()

    response_thoughts = []

    for mythout in myThoughts:

        if mythout.public == 1:

            if mythout.user.id == 2:

                response_thoughts.append(
                    {
                        "id": mythout.id,
                        "user": {
                            "id" : mythout.user.id,
                            "name" : mythout.user.name,
                            "active" : mythout.user.active,
                        },
                        "message": mythout.message,
                        "user_auth": True,
                        "like": mythout.like,
                        "edited": mythout.edited,  
                        "publish": mythout.publish,
                    })
            else: 
                response_thoughts.append(
                    {
                        "id": mythout.id,
                        "message": mythout.message,
                        "like": mythout.like,
                        "user_auth": False,
                        "publish": mythout.publish,
                    })        
            
    return JsonResponse(response_thoughts, safe=False)    

