from django.urls import path
from . import views

urlpatterns = [

    path('',views.createStudents,name='student'),
       path('home/',views.getStudents,name='home')
]