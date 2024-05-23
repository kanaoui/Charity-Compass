from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def causes(request):
    return render(request,'campagne/campagne_list.html')