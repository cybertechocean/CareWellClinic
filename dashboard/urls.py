from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_index, name='dashboard'),
    path('api/chart-data/', views.api_chart_data, name='api_chart_data'),
    path('appointments/', views.appointments_list, name='appointments'),
    path('patients/', views.patients_list, name='patients'),
    path('doctors/', views.doctors_list, name='doctors'),
    path('services/', views.services_list, name='services'),
    path('prescriptions/', lambda r: views.generic_subpage(r, 'prescriptions', 'Prescriptions'), name='prescriptions'),
    path('billing/', lambda r: views.generic_subpage(r, 'billing', 'Billing'), name='billing'),
    path('payments/', lambda r: views.generic_subpage(r, 'payments', 'Payments'), name='payments'),
    path('reports/', lambda r: views.generic_subpage(r, 'reports', 'Reports'), name='reports'),
    path('messages/', lambda r: views.generic_subpage(r, 'messages', 'Messages'), name='messages'),
    path('settings/', lambda r: views.generic_subpage(r, 'settings', 'Settings'), name='settings'),
]
