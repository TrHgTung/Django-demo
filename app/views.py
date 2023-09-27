from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        date=request.POST.get('date')
        provider=request.POST.get('provider')
        category=request.POST.get('category')
        print(name,desc,date,provider,category)

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")