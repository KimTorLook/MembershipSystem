"""
URL configuration for MembershipSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
from myapp import views

urlpatterns = [
    re_path(r'^admin', admin.site.urls),
    re_path(r'^$', views.sayhello),
    re_path(r'^index/$', views.index),
    re_path(r'^test/(\w+)/$', views.test),
    re_path(r'^backstage/$', views.backstage),
    re_path(r'^showpic/$', views.showpic),
    re_path(r'^listall/$', views.listall),
    re_path(r'^post/$', views.post),
    re_path(r'^post1/$', views.post1),
    re_path(r'^postform/$', views.postform),
    re_path(r'^delete/(\d+)/$', views.delete),
    re_path(r'^edit/(\d+)/edit/$', views.edit),
    re_path(r'^login/$', views.login),
    ]