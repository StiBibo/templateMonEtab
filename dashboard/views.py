from django.shortcuts import render

# Create your views here.


def homeDashboard(request):
    return render(request, 'dashboard/index.html')