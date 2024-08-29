from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.


def homeEleve(request):
    students = Eleve.objects.all()
    context = {
        'students':students
    }
    return render(request, 'eleve/student_list.html',context)

def addStudent(request):
    students = StudentFormModel()
    if request.method == 'POST':
        students = StudentFormModel(request.POST)
        if students.is_valid():
            students.save()
            return redirect('student:student_list')
        
    context = {
        'students': students ,
        'title' : 'Ajouter eleve',
        } 
    return render(request, 'eleve/add_student.html', context)

def updateStudent(request, id):
    context = {
        'title':'Modifier eleve'
    }
    student = Eleve.objects.get(id=id)
    if request.method == 'POST':
        students = StudentFormModel(request.POST, instance=student) 
        if students.is_valid():
            students.save()
            return redirect('student:student_list')
        
    students = StudentFormModel(instance=student)
    context["students"] = students

    return render(request, 'eleve/add_student.html', context)

def delete_student(request, id):
    student = Eleve.objects.get(id=id)
    student.delete() 
    return redirect('student:student_list')
