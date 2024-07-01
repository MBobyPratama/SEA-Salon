from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', include('register.urls')),
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('make-reservation/', views.make_reservation, name='make_reservation'),
    path('get-services/', views.get_services, name='get_services'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('get-branch-hours/', views.get_branch_hours, name='get_branch_hours'),
]
