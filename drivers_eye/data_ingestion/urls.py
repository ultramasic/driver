from django.urls import path
from .views import RawDataView, data_ingestion_view


urlpatterns = [
    path('raw-data/', RawDataView.as_view(), name='raw-data'),
    path('data_ingestion/', data_ingestion_view, name='data_ingestion'),
]


