from django.db import models


class Student(models.Model):
    matric = models.CharField(max_length=30, unique=True)
    lName = models.CharField(max_length=100)
    mName = models.CharField(max_length=100)
    fName = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.EmailField()
    course = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    entry = models.DateField()
    exit = models.DateField()
    state = models.CharField(max_length=30)

