from django.shortcuts import render,redirect
from .models import Campagne
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def campagne_list(request):
    campagnes = Campagne.objects.all()
    return render(request, 'campagne/campagne_list.html' , {'campagne' : campagnes})

def campagne_detail(request, slug):
    # return HttpResponse(slug)
    campagne = Campagne.objects.get(slug=slug)
    return render(request, 'campagne/campagne_detail.html', { 'campagne': campagne })

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateCampagne(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.fundraiser = request.user
            instance.save()
            return redirect('campagne:campagne_list')
    else:
        form = forms.CreateCampagne()
    return render(request,'campagne/campagne_create.html', {'form': form})