from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from myapp.models import Craftsman
from myapp.form import PostForm
from random import randint
import os

def sayhello(request):
    return HttpResponse("Hello Django!")

def employeelist(request, id=None):
    craftsman = Craftsman.objects.all().order_by('cId')         #提取所有員工的資料
    return render(request, "employeelist.html", locals())

def showpic(request):                                           #沒有用
    all_files = os.listdir('static\images')
    return render(request, "showpic.html", locals())

def listall(request):                                           #沒有用
    try:
        unit = Craftsman.objects.all().order_by('id')
    except:
        erromessage = "(erromessage)"
    return render(request, "listall.html", locals())
  
     

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


def post(request):                          #沒有用
    if request.method == "POST":
        mess=request.POST['username']
    else:
        mess="表單資料尚未送出！"
    return render(request, "post.html", locals())


def post1(request):                         #新增員工表格
    if request.method == "POST":            #先檢查方法
        postform = PostForm(request.POST)   #將標頭的資料帶到postform作資料形別的驗證
        if postform.is_valid():             #如果所有資通過驗證
            cId = postform.cleaned_data['cId']
            cName = postform.cleaned_data['cName']
            cSex = postform.cleaned_data['cSex']
            cBirthday = postform.cleaned_data['cBirthday']
            cEmail = postform.cleaned_data['cEmail']
            cPhone = postform.cleaned_data['cPhone']
            cAddr = postform.cleaned_data['cAddr']    #所有資料會儲存到資料庫中
            unit=Craftsman.objects.create(cId=cId, cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
            message = "己儲存..."
            return redirect('/employeelist/')
        else:                               #如果所有資通過驗證                
            message = "驗證碼錯誤！"
    else:
        message = "姓名、性別、生日必須輸入！"  #如果進入網頁的方法不是post
        postform = PostForm(request.POST)
    return render(request, "post1.html", locals())


def postform(request):  #新增資料，資料必須驗證
    postform = PostForm(request.POST)
    return render(request, "postform.html", locals())		


def delete(request, id=None):             #在employee網頁中可以刪除員工資料
    if id!=None:                          #URL需要有員工ID
        if request.method == "POST":
            id = request.POST['cId']
        try:
            unit=Craftsman.objects.get(cId=id)
            unit.delete()
            return redirect('/employeelist/')
        except:
            message = "讀取錯誤"
    return render(request, "delete.html", locals())  


def edit(request, id=None, mode=None):
    if mode == "edit":                       #URL有第三個元素mode
        unit=Craftsman.objects.get(cId=id)   #提取資料
        unit.cName=request.GET.get('cName', unit.cName)
        unit.cSex=request.GET.get('cSex', unit.cSex)
        unit.cBirthday=request.GET.get('cBirthday', unit.cBirthday)
        unit.cEmail=request.GET.get('cEmail', unit.cEmail)
        unit.cPhone=request.GET.get('cPhone', unit.cPhone)
        unit.cAddr=request.GET.get('cAddr', unit.cAddr)
        unit.save()
        message = "己修改..."
        return redirect('/employeelist/')
    else:
        try:
            unit = Craftsman.objects.get(cId=id)
            strdate=str(unit.cBirthday)
            strdate2=strdate.replace("年","-")   #更改日期的格式
            strdate2=strdate.replace("月","-")
            strdate2=strdate.replace("日","-")
            unit.cBirthday = strdate2
        except:
            message = "此id不存在!"
        return render(request, "edit.html", locals())
    
def edit2(request, id=None, mode=None):
    if mode == "load":
        unit = Craftsman.objects.get(cId=id)
        strdate=str(unit.cBirthday)
        strdate2=strdate.replace("年","-")
        strdate2=strdate.replace("月","-")
        strdate2=strdate.replace("日","-")
        unit.cBirthday = strdate2
        return render(request, "edit2.html", locals())
    elif mode == "save":
        unit = Craftsman.objects.get(cId=id)
        unit.cName=request.POST["cName"]
        unit.cSex=request.POST["cSex"]
        unit.cBirthday=request.POST["cBirthday"]
        unit.cEmail=request.POST["cEmail"]
        unit.cPhone=request.POST["cPhone"]
        unit.cAddr=request.POST["cAddr"]
        unit.save()
        message = '己修改...'
        return redirect('/employeelist/')
    return render(request, "edit2.html", locals()) #自創

def index(request):
    try:                    #這個try except沒有用
        if User.objects.session == True:
            pass
    except:
        pass                                   
    return render(request, "index.html", locals())

            

def login(request):
    if request.method == 'POST':                    #先驗查方法
        name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=name, password = password)  #核對帳密
        if user is not None:                        #核對成功時
            if user.is_active:                      #驗查用戶是否活躍
                auth.login(request,user)
                message = '登入成功！'
                return redirect('/index/')
            else:
                message = '帳號尚未啟用！'
        else:
            message = '登入失敗！'
    return render(request, "login.html", locals())

def logout(request):
    auth.logout(request)
    return redirect("/index/")
    

def adduser(request):              #沒有用     
    try:
        user=User.objects.get(username="test")
    except:
        user=None
    if user!=None:
        message = user.username + "帳號己建立！"
        return HttpResponse(message)
    else:
        user = User.objects.create_user("test", "test.test.com.tw","aa123456")
        user.first_name="wen"
        user.last_name="lin"
        user.is_staff=True
        user.save()
        return redirect('/admin/')