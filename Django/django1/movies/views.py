from django.shortcuts import render,redirect
from .models import Movieinfo
from .forms import MovieForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def create(request):
    if request.POST:
        form=MovieForm(request.POST,request.FILES)
        print(request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form=MovieForm()
    return render(request,'create.html',{'form':form})

def edit(request,id):
    to_Edit=Movieinfo.objects.get(id=id)
    form=MovieForm(request.POST,instance=to_Edit)
    if form.is_valid():
        to_Edit.save()
        return redirect('/list')
    form=MovieForm(instance=to_Edit)
    return render(request,'edit.html',{'form':form})

def delete(request,id):
    D=Movieinfo.objects.get(id=id)
    D.delete()
    movie_data=Movieinfo.objects.all()
    return render(request,'list.html',{'movies':movie_data})

def list(request):
    movie_data=Movieinfo.objects.all()
    return render(request,'list.html',{'movies':movie_data})