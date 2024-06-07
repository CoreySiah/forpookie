from django.shortcuts import render, HttpResponse
from .models import CourseModuleItem

# Create your views here.

def home(request):
    return render(request, "home.html")

def modules(request):
    items = CourseModuleItem.objects.all()
    return render(request, "modules.html", {"modules": items})