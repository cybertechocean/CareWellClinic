from django.contrib import admin
from .models import Doctor, Patient, Service, Appointment, MonthlyRevenue, ClinicSetting


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'email', 'phone', 'is_active', 'joined_date')
    list_filter = ('is_active', 'specialization')
    search_fields = ('name', 'specialization', 'email')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'service', 'doctor', 'date', 'time_str', 'status')
    list_filter = ('status', 'date')
    search_fields = ('patient__name', 'service__name', 'doctor__name')


@admin.register(MonthlyRevenue)
class MonthlyRevenueAdmin(admin.ModelAdmin):
    list_display = ('month_name', 'year', 'amount', 'is_current_month')
    list_filter = ('year', 'is_current_month')


@admin.register(ClinicSetting)
class ClinicSettingAdmin(admin.ModelAdmin):
    list_display = ('clinic_name', 'currency_code', 'admin_name', 'admin_role')
