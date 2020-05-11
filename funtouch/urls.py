"""funtouch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',blog),
    path('blogalt/',blogalt),
    path('blogsingle/',blogsingle),
    path('casestudies/',casestudies),
    path('casestudiesalt/',casestudiesalt),
    path('casestudiessingle/',casestudiessingle),
    path('index/',index),
    path('page/',page),
    path('pageabout/',pageabout),
    path('pageclients/',pageclients),
    path('pagecontact/',pagecontact),
    path('pagecontactalt/',pagecontactalt),
    path('pageebooks/',pageebooks),
    path('pagefaqs/',pagefaqs),
    path('pagefullwidth/',pagefullwidth),
    path('pagenotfound/',pagenotfound),
    path('pagepricing/',pagepricing),
    path('pageseoanalysis/',pageseoanalysis),
    path('pageservices/',pageservices),
    path('pagetestimonials/',pagetestimonials),
    path('service01/',service01),
    path('service02/',service02),
    path('service03/',service03),
    path('service04/',service04),
    path('service05/',service05),
    path('service06/',service06),
    path('service07/',service07),
    path('service08/',service08),
    path('service09/',service09),
]
