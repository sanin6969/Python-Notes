from django.db import models

# Create your models here.
class Teacher(models.Model):
    fistname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    
    def __str__(self) :
        return self.fistname
    
class Student(models.Model):
    fistname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField()    
    classroom=models.IntegerField()    
    teacher=models.CharField(max_length=150)
    
    def __str__(self):
        return self.fistname