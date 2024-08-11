from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_driver, name='create_driver'),
    path('<int:driver_id>/', views.driver_profile, name='driver_profile'),
    path('<int:driver_id>/edit/', views.edit_driver, name='edit_driver'),
    path('<int:pk>/delete/', views.delete_driver, name='delete_driver'),
]
