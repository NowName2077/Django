from django.shortcuts import render
from .models import Student, Group
from django.db.models import Q, Count
# Create your views here.
def home(request):
    context = {}
    return render(request, 'myapp/home.html', context)

def about(request):
    context = {}
    return render(request, 'myapp/about.html', context)

def students(request):
    students_all = Student.objects.all()
    context = {
        "students_all": students_all
               }
    return render(request, 'myapp/students.html', context)
