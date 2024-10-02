from django.contrib import admin  # Importing Django's admin module, which allows registering models for the admin interface
from .models import Location, Item  # Importing the Location and Item models from the current app's models.py file

# Registering the Location model with the admin site so that it can be managed through the Django admin interface
admin.site.register(Location)

# Registering the Item model with the admin site for management through the admin interface
admin.site.register(Item)