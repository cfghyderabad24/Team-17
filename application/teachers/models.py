from django.db import models

class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=100)
    teacher_name=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.Username
    

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    grade=models.IntegerField()
    level=models.IntegerField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    timestamps=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'genre_table'

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=100, blank=False)
    isbn_code = models.CharField(max_length=100, blank=False, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    available_copies = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'book_table'

    def __str__(self):
        return self.name

class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=100, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'checkout_table'

    def __str__(self):
        return f"{self.student_id} - {self.book.name}"

class Checkin(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=100, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkin_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'checkin_table'

    def __str__(self):
        return f"{self.student_id} - {self.book.name}"
