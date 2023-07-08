from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def skills(request):
    return render(request,'skills.html')

def award(request):
    return render(request,'award.html')

def about(request):
    return render(request,'about.html')