from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.

def home_teacher(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teacher/list_teacher.html', context)

def add_teacher(request):
    teachers = TeacherFormModel()
    if request.method == 'POST':
        teachers = TeacherFormModel(request.POST)
        if teachers.is_valid():
            teachers.save()
            return redirect('teacher:list_teacher') 

    context = {
        'teachers':teachers,
        'title' : 'Ajouter professeur'
        } 
    return render(request, 'teacher/add_teacher.html', context)

def update_teacher(request, id):
    context = {
        'title' : 'Modifier professeur'
    }
    teacher = Teacher.objects.get(id = id)
    if request.method == 'POST':
        teacher_form = TeacherFormModel(request.POST, instance=teacher)
        if teacher_form.is_valid():
            print(f"teacher_form : {teacher_form}")
            teacher_form.save()
            return redirect('teacher:list_teacher') 
    
    teacher_form = TeacherFormModel(instance=teacher)
    context["teachers"] = teacher_form
    return render(request, 'teacher/add_teacher.html', context)

def delete_teacher(request, id):
    teacher = Teacher.objects.get(id = id )
    teacher.delete()
    return redirect('teacher:list_teacher')
