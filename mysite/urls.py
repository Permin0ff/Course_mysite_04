"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('blog.urls', namespace='blog')),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views.sitemap'),
                  path("accounts/", include("accounts.urls")),
                  path("accounts/", include("django.contrib.auth.urls")),
                  re_path(r'^oauth/', include('social_django.urls', namespace='social')),
                  path('summernote/', include('django_summernote.urls')),
                  path("api/", include("blog_api.urls")),  # new
                  path("api-auth/", include("rest_framework.urls")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
