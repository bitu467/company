from django.db import models

# Create your models here.


class Dept(models.Model):
    ID = models.BigAutoField(primary_key=True, auto_created=True)
    Code = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Create_user = models.TextField(null=True)
    Create_Date = models.DateField(null=True)


class Employee(models.Model):
    ID = models.BigAutoField(primary_key=True, auto_created=True)
    ECode = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    DOB = models.DateField()
    Dept = models.CharField(max_length=255)
    salary = models.BigIntegerField()
