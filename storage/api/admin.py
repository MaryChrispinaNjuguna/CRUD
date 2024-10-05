from django.contrib import admin  # Importing Django's admin module, which allows registering models for the admin interface
from .models import Location, Item  # Importing the Location and Item models from the current app's models.py file

# Registering models with the admin site so that it can be managed through the Django admin interface
admin.site.register(Location)
admin.site.register(Item)