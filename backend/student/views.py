from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from .models import student
from .forms import studentForm


def createStudents(request):
      form=studentForm()
      context={'form':form}
      if request.method=='POST':
            form=studentForm(request.POST)
            if form.is_valid():
                  form.save()
                  print('hrllow')
                  return redirect("home")
      return render(request,'student_form.html',context)
def getStudents(request):
    students=student.objects.all()
    return render(request,'home.html',{'students':students})




