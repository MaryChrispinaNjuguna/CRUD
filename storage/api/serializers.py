from rest_framework import serializers  # Importing the serializers module from Django Rest Framework
from .models import Item, Location  # Importing the Item and Location models

# Serializer for the Item model
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item  # Specifies the model that this serializer is associated with (Item)
        fields = ('__all__')  # Tells the serializer to include all fields of the Item model

# Serializer for the Location model
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location  # Specifies the model that this serializer is associated with (Location)
        fields = ('__all__')  # Tells the serializer to include all fields of the Location model
