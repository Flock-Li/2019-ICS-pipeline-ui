"""simulator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include

from simulator.views import main 
from simulator import views

urlpatterns = [
    #额外的参数将给到view.py中作为参数，字典信息，给url模式命名，
    #index访问url=8000/index/
    path('admin/', admin.site.urls),
    path("",main),
    path("load/",views.load),
    path("step/",views.step),
    path("comment/",views.comment),
    path("postcomment/",views.postcomment),
    path("add/",views.add),
]
