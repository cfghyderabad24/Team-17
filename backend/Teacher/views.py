from django.shortcuts import render,redirect
from .models import Teacher
from .forms import TeacherForm
# Create your views here.

def createTeacher(request):
    form=TeacherForm()

    if request.method=='POST':
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'teacher_form.html',{'form':form})

def getTeacher(request):
    teacher=Teacher.objects.all()
    return render(request,'homepage.html',{'teachers':teacher})