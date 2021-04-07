from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from user import models


def joinform(request):
    return render(request,'user/joinform.html')

def joinsuccess(request):
    return render(request,'user/joinsuccess.html')

def join(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']

    models.insert(name, email, password, gender)

    return HttpResponseRedirect('/user/joinsuccess')

def loginform(request):
    return render(request, 'user/loginform.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    result = models.findby_email_and_password(email, password)
    if result is None:
        return HttpResponseRedirect('/user/loginform?result=fail')

    # login
    request.session["authuser"] = result

    return HttpResponseRedirect('/')

def logout(request):
    del request.session["authuser"]
    return HttpResponseRedirect('/')

def updateform(request):
    # access control
    if 'authuser' not in request.session: # python code
        return HttpResponseRedirect('/')

    authuser = request.session["authuser"]
    result = models.findbyno(authuser["no"])
    return render(request, 'user/updateform.html')

def update(request):
    pass