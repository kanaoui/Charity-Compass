from django.shortcuts import render


# Create your views here.


def donate_view(request):
    return render(request,'donate/donate.html')
