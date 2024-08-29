from django.shortcuts import redirect, render
from .forms import *
from . import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def list_user(request):

    users = User.objects.all()
    context = {
        'users': users
    }
    print(f"")
    return render(request, 'user/list_user.html', context)

def add_user(request):
    form = UserFormsModel()
    if request.method == 'POST':
        form = UserFormsModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:list_user')


    context = {
        'user_form':form,
        'title': 'Ajouter utilisateur'
    }
    # return render(request, 'user/add_user.html',context)
    return render(request, 'user/forms.html',context)


def update_user(request, id):
    context = {
        'title': 'Modifier utilisateur'
    }
    user = User.objects.get(id = id)
    if request.method == 'POST':
        user_form = UserFormsModel(request.POST, instance=user) 
        if user_form.is_valid():
            print(f"user_form : {user_form}")
            user_form.save()
            return redirect('user:list_user') 
    
    user_form = UserFormsModel(instance=user)
    context["user_form"] = user_form

    # return render(request, 'user/update_user.html', context)
    return render(request, 'user/forms.html',context)


def delete_user(request, id):
    user = User.objects.get(id = id ) 
    user.delete()
    return redirect('user:list_user') 

def add_auth_user(request):
    if request.method == 'POST':
        pseudo = request.POST["username"]
        password = request.POST["password"]
        if not pseudo or not password:
            print(f"Nous sommes ici !")
            return redirect('user:add_user')


        user = User(username = pseudo)
        user.save()
        user.password = password
        user.set_password(user.password)
        user.save()
    context = {
        'title': 'Ajouter utilisateur'
    }

    return render(request, 'user/forms.html',context)
    

