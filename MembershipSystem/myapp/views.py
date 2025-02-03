from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
from myapp.models import Craftsman
import os
from myapp.form import PostForm

def sayhello(request):
    return HttpResponse("Hello Django!")

def index(request, id=None):
    craftsman = Craftsman.objects.all().order_by('id')
    return render(request, "index.html", locals())

def showpic(request):
    all_files = os.listdir('static\images')
    return render(request, "showpic.html", locals())

def listall(request):
    try:
        unit = Craftsman.objects.all().order_by('id')
    except:
        erromessage = "(erromessage)"
    return render(request, "listall.html", locals())

def backstage(request):
    return render(request, "backstage.html", locals())

#def index(request, username):
     
     

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


def post(request):
    if request.method == "POST":
        mess=request.POST['username']
    else:
        mess="表單資料尚未送出！"
    return render(request, "post.html", locals())


def post1(request):
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            cId = postform.cleaned_data['cId']
            cName = postform.cleaned_data['cName']
            cSex = postform.cleaned_data['cSex']
            cBirthday = postform.cleaned_data['cBirthday']
            cEmail = postform.cleaned_data['cEmail']
            cPhone = postform.cleaned_data['cPhone']
            cAddr = postform.cleaned_data['cAddr']
            unit=Craftsman.objects.create(cId=cId, cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
            message = "己儲存..."
            return redirect('/index/')
        else:
            message = "驗證碼錯誤！"
    else:
        message = "姓名、性別、生日必須輸入！"
        postform = PostForm(request.POST)
    return render(request, "post1.html", locals())


def postform(request):  #新增資料，資料必須驗證
    postform = PostForm(request.POST)
    return render(request, "postform.html", locals())		


def delete(request, id=None):
    if id!=None:
        if request.method == "POST":
            id = request.POST['cId']
        try:
            unit=Craftsman.objects.get(id=id)
            unit.delete()
            return redirect('/index/')
        except:
            messagew = "讀取錯誤"
    return render(request, "delete.html", locals())  


def edit(request, id=None, mode=None):
    if mode == "edit":
        unit=Craftsman.objects.get(id=id)
        unit.cName=request.GET.get('cName', unit.cName)
        unit.cSex=request.GET.get('cName', unit.cSex)
        unit.cBirthday=request.GET.get('cName', unit.cBirthday)
        unit.cEmail=request.GET.get('cName', unit.cEmail)
        unit.cPhone=request.GET.get('cName', unit.cPhone)
        unit.cAddr=request.GET.get('cName', unit.cAddr)
        unit.save
        messagew = "己修改..."
        return redirect('/index/')
    else:
        try:
            unit = Craftsman.objects.get(id=id)
            strdate=str(unit.cBirthday)
            strdate2=strdate.replace("年","-")
            strdate2=strdate.replace("月","-")
            strdate2=strdate.replace("日","-")
            unit.cBirthday = strdate2
        except:
            message = "此id不存在!"
        return render(request, "edit.html", locals())
            

def login(request):
     
     return render(request, "login.html", locals())

