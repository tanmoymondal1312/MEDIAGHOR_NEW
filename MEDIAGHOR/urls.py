"""
URL configuration for MEDIAGHOR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import include, path
from .sitemaps import StaticViewSitemap
from Resources.sitemaps import LibrarySitemap
from . import views
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'libraries': LibrarySitemap,
}


urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('users/', include('Users.urls', namespace='users')),
    path('resources/', include('Resources.urls', namespace='resources')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
