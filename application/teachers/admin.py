from django.contrib import admin
from .models import Teacher,Student,Book,Genre,Checkin,Checkout

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Checkout)
admin.site.register(Checkin)