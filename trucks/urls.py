from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_truck, name='create_truck'),
    path('<int:pk>/', views.truck_profile, name='truck_profile'),
    path('<int:pk>/edit/', views.edit_truck, name='edit_truck'),
    path('<int:pk>/delete/', views.delete_truck, name='delete_truck'),
    path('truck-data/', views.truck_data, name='truck_data'),
]
