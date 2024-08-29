from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('student/', views.homeEleve, name='student_list'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('update_student/<int:id>', views.updateStudent, name='update_student'),
    path('delete_student/<int:id>', views.delete_student, name='delete_student'), 



]
