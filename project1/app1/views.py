from django.shortcuts import render, HttpResponse
from .models import Details
# Create your views here.

def index(request):
    if request.method == 'POST':
       type = request.POST['type'] 
       name = request.POST['name']
       college = request.POST['college']
       branch = request.POST['branch']
       year = request.POST['year']
       print(type,name)
       obj = Details()
       obj.type = type
       obj.name = name
       obj.college = college
       obj.branch = branch
       obj.year = year
       obj.save()
    context = {

    }
    return render(request , 'index.html',context)

def next(request):
    return render(request , 'anotherpage.html')

def course(request):
    return render(request , 'course.html')