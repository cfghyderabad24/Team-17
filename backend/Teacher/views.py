from django.shortcuts import render,redirect
from .models import Teacher
from .forms import Form
# Create your views here.

def CreateForm(request):
    form=Form(request.POST)
    if request.method=='POST':
        form=Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'form.html',{'form':form})

def getTeachers(request):
    teacher=Teacher.objects.all()
    return render(request,'home.html',{'teachers':teacher})