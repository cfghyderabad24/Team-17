from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from .models import student



class studentForm(ModelForm):
    class Meta:
        model=student
        fields='_all_'

def createStudent(request):
      form=studentForm()
      context={'form':form}
      if request.method=='POST':
            form=studentForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect("home")
      return render(request,'student_form.html',context)




