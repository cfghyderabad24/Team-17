from django.urls import path
from . import views

urlpatterns=[
    path('',views.CreateForm,name='create'),
    path('home/',views.getTeachers,name='homepage')
]