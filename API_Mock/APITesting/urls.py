
from django.contrib import admin
from django.urls import path,include,re_path
from APITesting import views


urlpatterns = [

    re_path('test$',views.index),
]
