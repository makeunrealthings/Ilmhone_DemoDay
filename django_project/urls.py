# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new
urlpatterns = [
    path("", include("pages.urls")), # new
    path("admin/", admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),  # Add this line
    path("accounts/", include("accounts.urls")), # new
    path("accounts/", include("django.contrib.auth.urls")), # new
     path("articles/", include("articles.urls")), # new

    path("", TemplateView.as_view(template_name="home.html"),
    
        name="home"),
]