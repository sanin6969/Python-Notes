from django.shortcuts import render
from .models import Student
# Create your views here.
def student_list(request):
    posts=Student.objects.all()
    print(posts)
    
    return render(request,'output.html',{'post':posts})