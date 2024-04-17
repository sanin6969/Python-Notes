from django.db import models

# Create your models here.
# class character(models.Model):
#     main=models.CharField(max_length=100)
#     side=models.CharField(max_length=100)
    
class Movieinfo(models.Model):
    title=models.CharField(max_length=200)
    year=models.IntegerField(null=True)
    rating=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/',null=True)
    # details=models.OneToOneField(character,on_delete=models.SET_NULL,related_name='movie' ,null=True)
    def __str__(self):
        return self.title
