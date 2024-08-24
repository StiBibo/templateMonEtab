from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('list_user', views.list_user, name='list_user'),
    path('add_user', views.add_user, name='add_user'),
    path('update_user', views.update_user, name='update_user'),


]