from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book
# Create your views here.
def index(request):
    data = Book.objects.all()
    context = {"data" : data}
    return render(request,"index.html",context)

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        date=request.POST.get('date')
        provider=request.POST.get('provider')
        category=request.POST.get('category')
        print(name,desc,date,provider,category)
        query=Book(name=name,desc=desc,date=date,provider=provider,category=category)
        query.save()
    # return render(request,"index.html")
    return HttpResponseRedirect('/')

def updateData(request,id):
    d = Book.objects.get(id=id)
    context = {"d" : d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    data = Book.objects.all()
    context = {"data" : data}
    return render(request,"index.html",context)
    # return HttpResponseRedirect('/')

def about(request):
    return render(request,"about.html")