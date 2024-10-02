"""
URL configuration for storage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin  # Importing the admin module to configure admin-related URLs
from django.urls import path, include  # Importing path and include for defining URL patterns and including app-specific URLs

# Defining the main URL patterns for the project
urlpatterns = [
    # URL pattern for accessing the Django admin interface
    path('admin/', admin.site.urls),

    # URL pattern for including the URLs from the 'api' app
    # This will include all the URL patterns defined in 'api.urls'
    # The root path ('') means these URLs will be accessed at the root of the website
    path('', include('api.urls')),
]

