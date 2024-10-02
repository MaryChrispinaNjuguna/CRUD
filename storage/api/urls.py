from django.urls import path  # Importing the path function to define URL patterns
from .views import LocationList, LocationDetail, ItemList, ItemDetail  # Importing view classes to be used in the URL patterns

# Defining URL patterns for the app
urlpatterns = [
    # URL pattern for listing all locations or creating a new location
    # Maps to the LocationList view (GET and POST requests)
    path('location/', LocationList.as_view()),

    # URL pattern for retrieving, updating, or deleting a specific location by its primary key (pk)
    # Maps to the LocationDetail view (GET, PUT, PATCH, DELETE requests)
    path('location/<int:pk>/', LocationDetail.as_view()),

    # URL pattern for listing all items or creating a new item
    # Maps to the ItemList view (GET and POST requests)
    path('item/', ItemList.as_view()),

    # URL pattern for retrieving, updating, or deleting a specific item by its primary key (pk)
    # Maps to the ItemDetail view (GET, PUT, PATCH, DELETE requests)
    path('item/<int:pk>/', ItemDetail.as_view()),
]
