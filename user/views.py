from django.shortcuts import render
from .forms import *

# Create your views here.


def list_user(request):
    return render(request, 'user/list_user.html')

def add_user(request):
    if request.method == 'POST':
        print(f"request post : {request.POST}")
        form = UserFormsModel(request.POST)
        if form.is_valid():
            # print(f"form : {form} ")
            form.save()
    
    context = {'form':form}
    print(f"context : {context} " )
    return render(request, 'user/add_user.html',context)

def update_user(request):
    return render(request, 'user/update_user.html')