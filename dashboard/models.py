from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField(max_length=120)
    specialization = models.CharField(max_length=120)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    avatar = models.CharField(max_length=255, blank=True, default='')
    joined_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.specialization})"


class Patient(models.Model):
    name = models.CharField(max_length=120)
    gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Female')
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=30, blank=True, default='')
    email = models.EmailField(blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=30, blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField(default=timezone.now)
    time_str = models.CharField(max_length=20, default='09:00 AM')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Confirmed')
    notes = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date', 'time_str']

    def __str__(self):
        return f"{self.patient.name} - {self.service.name} ({self.status})"


class MonthlyRevenue(models.Model):
    month_name = models.CharField(max_length=20)
    month_num = models.PositiveSmallIntegerField(default=1)
    year = models.PositiveIntegerField(default=2025)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    is_current_month = models.BooleanField(default=False)

    class Meta:
        ordering = ['year', 'month_num']

    def __str__(self):
        return f"{self.month_name} {self.year}: KES {self.amount}"


class ClinicSetting(models.Model):
    clinic_name = models.CharField(max_length=120, default='CareWell Clinic')
    tagline = models.CharField(max_length=255, default='Healthcare Management Dashboard')
    currency_code = models.CharField(max_length=10, default='KES')
    admin_name = models.CharField(max_length=100, default='Admin')
    admin_role = models.CharField(max_length=100, default='Administrator')

    def __str__(self):
        return self.clinic_name
