from core.models import Restaurent,Rating
from django.db import connection
from django.utils import timezone
from django.contrib.auth.models import User
def run():
    # restaurent=Restaurent()
    # restaurent.name='albushra hotel'
    # restaurent.latitude=49.94
    # restaurent.longitude=90.76
    # restaurent.date_opened=timezone.now()
    # restaurent.restaurent_type=restaurent.TypeChoices.INDIAN
    # restaurent.save()
    
    # nother one
    # Restaurent.objects.create(
    #     name='crispy pastas',
    #     date_opened=timezone.now(),
    #     restaurent_type=Restaurent.TypeChoices.ITALIAN,
    #     latitude=60.89,
    #     longitude=67.67
    # )
    
    restaurent=Restaurent.objects.first()
    user=User.objects.first()
    Rating.objects.create(user=user,restaurent=restaurent,rating=3)
    