from django.urls import path
from . import views

urlpattern=[
    path('',views.getTeacher,name='homepage'),
    path('/create',views.createTeacher,name='create')
]