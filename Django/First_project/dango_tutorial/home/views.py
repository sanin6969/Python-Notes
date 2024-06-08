from django.shortcuts import render
from .models import Departments,Doctors
from .forms import Booking_Form
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    form=Booking_Form()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    Dict_doc={
        'doc':Doctors.objects.all()
    }
    return render(request,'doctors.html',Dict_doc)

def Contact(request):
    return render(request,'contact.html')

def department(request):
    Dict_dep={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',Dict_dep)
