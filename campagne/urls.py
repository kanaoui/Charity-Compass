from django.urls import path, re_path
from . import views

app_name = 'campagne'

urlpatterns = [
    path('',views.campagne_list, name="campagne_list"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.campagne_detail, name="detail"),
]

