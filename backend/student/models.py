from django.db import models

class student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255,null=True)
    grade=models.IntegerField(max_length=100,null=True)
    no_of_books_checked_in=models.IntegerField(max_length=13,null=True)
    timeStamp=models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return "details of "+self.name
