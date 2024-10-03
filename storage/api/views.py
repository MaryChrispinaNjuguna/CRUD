from rest_framework import generics  # Import Django Rest Framework's generic views

from .models import Location, Item  # Importing the Location and Item models
from .serializers import LocationSerializer, ItemSerializer  # Importing the serializers for Location and Item models

# This class handles listing and creating new items.
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer  # Specifies the serializer used for this view (ItemSerializer)

    # Method to retrieve the queryset for the view
    def get_queryset(self):
        queryset = Item.objects.all()  # Retrieve all items from the database
        location = self.request.query_params.get('location')  # Get 'location' from query parameters in the URL
        if location is not None:  # If the 'location' parameter exists in the request
            queryset = queryset.filter(location=location)  # Filter items by location
        return queryset  # Return the filtered or full queryset

# This class handles retrieving, updating, and deleting a single item by ID.
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()  # Retrieve all items, required by Django Rest Framework
    serializer_class = ItemSerializer  # Specifies the serializer used for this view (ItemSerializer)

# This class handles listing and creating new locations.
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()  # Retrieve all locations from the database
    serializer_class = LocationSerializer  # Specifies the serializer used for this view (LocationSerializer)

# This class handles retrieving, updating, and deleting a single location by its ID.
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()  # Retrieve all locations, required by Django Rest Framework
    serializer_class = LocationSerializer  # Specifies the serializer used for this view (LocationSerializer)
