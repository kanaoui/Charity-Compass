from django.shortcuts import render
from campagne.models import Campagne

# Create your views here.


def donate_view(request):
    return render(request,'donate/donate.html')

def donate_detail(request, slug):
    # return HttpResponse(slug)
    campagne = Campagne.objects.get(slug=slug)
    return render(request, 'donate/donate.html', { 'campagne': campagne })