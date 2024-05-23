from django.urls import path, re_path
from . import views

app_name='donate'


urlpatterns=[
    re_path(r'^donate/$',views.donate_view, name="donate"),
]