from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from myapp.models import Craftsman
import os

def sayhello(request):
    return HttpResponse("Hello Django!")

def showpic(request):
    all_files = os.listdir('static\images')
    return render(request, "showpic.html", locals())

def listall(request):
    try:
        unit = Craftsman.objects.all().order_by('id')
    except:
        erromessage = "(erromessage)"
    return render(request, "backstage.html", locals())

def backstage(request):
    return render(request, "backstage.html", locals())



times = 0
def test(request, username):
    dice={"no":randint(1,6)}
    username = username
    global times
    times += 1
    local_times = times
    lista = range(1,6)
    person1 = {"name":"Amy","phone":"049-1234567","age":"20"}
    person2 = {"name":"Jacky","phone":"02-4455666","age":"25"}
    person3 = {"name":"Nacy","phone":"04-9876543","age":"17"}
    person =[person1, person2, person3]
    thing = [852123456789, 852987654321, "i'm using Django      ", "2017年6月13日 15:10", '', '<p>asd\n<br/>fls</p>', ]
    return render(request, "backstage.html", locals())