from django.urls import path # type: ignore
from . import views


app_name = 'teacher'

urlpatterns = [
    path('list_teacher/', views.home_teacher, name='list_teacher'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('update_teacher/', views.update_teacher, name='update_teacher'),

]
