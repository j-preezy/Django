from django.shortcuts import render
from django.http import HttpResponse

from . models import Student, Teacher, School


# Create your views here.



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def students(request):
    student = Student.objects.all()
    return render(request, 'students.html',{"student": student})

def teachers(request):
    teacher = Teacher.objects.all()
    return render(request, 'teachers.html',{"teacher": teacher})

def schools(request):
    school = School.objects.all()
    return render(request, 'schools.html',{"school": school})

def insertstudents(request):
    return render(request, 'insertstudents.html')

