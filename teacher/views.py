from django.shortcuts import render
from .forms import TeacherForms

# Create your views here.

def home_teacher(request):
    return render(request, 'teacher/list_teacher.html')

def add_teacher(request):
    form = TeacherForms()
    context = {'form':form}
    return render(request, 'teacher/add_teacher.html', context)

def update_teacher(request):
    return render(request, 'teacher/update_teacher.html')
