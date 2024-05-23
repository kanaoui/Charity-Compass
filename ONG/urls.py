"""
URL configuration for ONG project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views
from campagne import views as campagne_views
from donate import views as donate_views


app_name = 'base'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.homepage,name='home'),
    path('about/', views.about, name='about' ),
    path('causes/', views.causes, name ='causes'),
    re_path(r'^accounts/',include("accounts.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r'^campagne/', include('campagne.urls')),
    re_path(r'donate/',include('donate.urls')),
    path('homepage/',views.homepage)
]
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)