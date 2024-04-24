from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Batch(models.Model):
    BATCH=(
        ('BCA','BCA'),
         ('MCA','MCA'),
         ('MBA','MBA'),
 
    )
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,choices=BATCH,blank=True,null=True)
    year = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Student(models.Model):
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    def __str__(self):
        return self.name



   
    