from django import forms

from . models import Booking

class Date_input(forms.DateInput):
    input_type='date'
class Booking_Form(forms.ModelForm):
    class Meta :
        model=Booking
        fields='__all__'
        widgets={
            'booking_date':Date_input
        }