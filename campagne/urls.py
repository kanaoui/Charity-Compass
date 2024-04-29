from django.urls import path, re_path
from . import views

app_name = 'campagne'

urlpatterns = [
    re_path(r'^$',views.campagne_list, name="campagne_list"),
    re_path(r'^create/$',views.article_create, name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.campagne_detail, name="detail"),
]

