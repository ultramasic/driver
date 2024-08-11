from django.contrib import admin
from django.urls import include, path
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trucks/', include('trucks.urls')),
    path('drivers/', include('drivers.urls')),
    path('assets/', include('assets.urls')),
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),
    path('register/', account_views.register, name='register'),
    path('register_company/', account_views.register_company, name='register_company'),
    path('forgot_password/', account_views.forgot_password, name='forgot_password'),
    path('dashboard/', account_views.dashboard, name='dashboard'),
    path('', account_views.login_view, name='login'),  # Direct root URL to login
    path('data-ingestion/', include('data_ingestion.urls')),
    path('Fleet_view/', account_views.fleet_view, name='fleet_view'),
]
