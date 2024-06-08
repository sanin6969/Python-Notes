from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurent(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN='IN','Indian'
        CHINESE='CH','Chinese'
        ITALIAN='IT','Italian'
        GREEK='GR','Greek'
        MEXICAN='MX','Mexican'
        FASTFOOD='FF','Fast Food'
        OTHER='OT','Other'
        
    name =models.CharField(max_length=150)
    website= models.URLField(default='')
    date_opened=models.DateField()
    latitude =models.FloatField()
    longitude =models.FloatField()
    restaurent_type=models.CharField(max_length=2,choices=TypeChoices.choices,default='')
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurent=models.ForeignKey(Restaurent,on_delete=models.CASCADE)
    rating=models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"Rating :{self.rating}"
    
    
class Sale(models.Model):
    restaurent=models.ForeignKey(Restaurent,on_delete=models.CASCADE)
    income=models.DecimalField(max_digits=8,decimal_places=2)
    datetime=models.DateTimeField()
    
    



    