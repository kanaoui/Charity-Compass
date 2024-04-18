from django.shortcuts import render
from .models import Campagne

# Create your views here.
def campagne_list(request):
    campagnes = Campagne.objects.all()
    return render(request, 'campagne/campagne_list.html' , {'campagne' : campagnes})

def campagne_detail(request, slug):
    # return HttpResponse(slug)
    campagne = Campagne.objects.get(slug=slug)
    return render(request, 'campagne/campagne_detail.html', { 'campagne': campagne })