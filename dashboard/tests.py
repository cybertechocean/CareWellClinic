from django.test import TestCase, Client
from django.urls import reverse
from .models import ClinicSetting, Doctor, Patient, Service, Appointment, MonthlyRevenue


class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.clinic = ClinicSetting.objects.create(
            clinic_name='CareWell Clinic',
            tagline='Healthcare Management Dashboard',
            currency_code='KES',
            admin_name='Admin',
            admin_role='Administrator'
        )
        self.doctor = Doctor.objects.create(
            name='Dr. Faith Muthoni',
            specialization='Cardiology',
            is_active=True
        )
        self.patient = Patient.objects.create(
            name='John Otieno',
            gender='Male'
        )
        self.service = Service.objects.create(
            name='General Checkup',
            price=2500.00
        )
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            service=self.service,
            time_str='09:00 AM',
            status='Confirmed'
        )
        self.revenue = MonthlyRevenue.objects.create(
            month_name='May',
            month_num=5,
            year=2025,
            amount=125600.00,
            is_current_month=True
        )

    def test_dashboard_index_status_code(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CareWell')
        self.assertContains(response, 'Welcome back, Admin')
        self.assertContains(response, 'Total Appointments')
        self.assertContains(response, '42')
        self.assertContains(response, 'KES 125,600')
        self.assertContains(response, 'John Otieno')

    def test_api_chart_data(self):
        response = self.client.get(reverse('api_chart_data') + '?period=week')
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIn('labels', json_data)
        self.assertIn('today', json_data)
        self.assertIn('yesterday', json_data)

    def test_navigation_subpages(self):
        pages = ['appointments', 'patients', 'doctors', 'services', 'prescriptions', 'billing', 'payments', 'reports', 'messages', 'settings']
        for page in pages:
            response = self.client.get(reverse(page))
            self.assertEqual(response.status_code, 200)
