from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('student/', views.homeEleve, name='student_list'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('update_student/', views.updateStudent, name='update_student'),


]
