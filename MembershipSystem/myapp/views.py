from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
from myapp.models import Craftsman
import os
from myapp.form import PostForm

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
    return render(request, "listall.html", locals())

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

def post(request):
    if request.method == "POST":
        mess=request.POST['username']
    else:
        mess="表單資料尚未送出！"
    return render(request, "post.html", locals())

def post1(request):  #新增資料，資料必須驗證
	if request.method == "POST":  #如果是以POST方式才處理
		postform = PostForm(request.POST)  #建立forms物件
		if postform.is_valid():			#通過forms驗證
			cName = postform.cleaned_data['username'] #取得表單輸入資料
			cSex =  postform.cleaned_data['sex']
			cBirthday =  postform.cleaned_data['birthday']
			cEmail = postform.cleaned_data['email']
			cPhone =  postform.cleaned_data['phone']
			cAddr =  postform.cleaned_data['address']
			#新增一筆記錄
			unit = Craftsman.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
			message = '已儲存...'
			return redirect('/index/')	
		else:
			message = '驗證碼錯誤！'	
	else:
		message = '姓名、性別、生日必須輸入！'
		postform = PostForm()
	return render(request, "post1.html", locals())		


def postform(request):  #新增資料，資料必須驗證
	return render(request, "postform.html", locals())		  