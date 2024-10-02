from django.db import models  # Importing the models module from Django, used to create database models

# Model for Location
class Location(models.Model):
    location_name = models.CharField(max_length=100, unique=True)  # Defines a 'location_name' field with a maximum length of 100 characters. 'unique=True' ensures no duplicate location names.

    def __str__(self):
        return self.location_name  # String representation of the Location model, which will return the name of the location

# Model for Item
class Item(models.Model):
    item_name = models.CharField(max_length=100)  # Defines an 'item_name' field with a maximum length of 100 characters
    date_added = models.DateField(auto_now_add=True)  # Automatically stores the date when the item was added
    item_location = models.ForeignKey(Location, on_delete=models.CASCADE)  # Defines a ForeignKey relationship to the Location model. 'on_delete=models.CASCADE' means if the related Location is deleted, the associated items will also be deleted.

    def __str__(self):
        return self.item_name  # String representation of the Item model, which will return the name of the item
