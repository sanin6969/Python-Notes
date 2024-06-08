from django.shortcuts import render,redirect
from .models import StudentDetails
# Create your views here.
def index(request):
    data=StudentDetails.objects.all()
    context={'data':data}
    return render(request,'index.html',context)

def insertData(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=StudentDetails(name=name,email=email,age=age,gender=gender)
        query.save() 
        return redirect('/')
    return render(request,'index.html')


def updateData(request,id):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        edit=StudentDetails.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save() 
        return redirect('/')
    
    d=StudentDetails.objects.get(id=id)
    context={'d':d}
    return render(request,'edit.html',context)

def deleteData(request,id):
    d=StudentDetails.objects.get(id=id)
    d.delete()
    return redirect('/')