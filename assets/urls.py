from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_asset, name='create_asset'),
    path('<int:pk>/', views.asset_profile, name='asset_profile'),
    path('<int:pk>/edit/', views.edit_asset, name='edit_asset'),
    path('<int:pk>/delete/', views.delete_asset, name='delete_asset'),
]
