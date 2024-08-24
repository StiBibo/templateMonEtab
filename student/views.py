from django.shortcuts import render
from .forms import StudentForms

# Create your views here.


def homeEleve(request):
    return render(request, 'eleve/student_list.html')

def addStudent(request):
    form = StudentForms()
    context = {'form':form}
    return render(request, 'eleve/add_student.html', context)

def updateStudent(request):
    return render(request, 'eleve/update_student.html')
