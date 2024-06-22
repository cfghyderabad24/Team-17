from django.db import models

# Create your models here.
class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    school_name=models.CharField(max_length=100)
    number_of_students=models.IntegerField()

    def __str__(self):
        return self.username