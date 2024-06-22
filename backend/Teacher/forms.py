from django.forms import ModelForm
from .models import Teacher

class Form(ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'