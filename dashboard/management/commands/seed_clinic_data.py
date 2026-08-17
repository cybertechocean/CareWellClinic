from django.core.management.base import BaseCommand
from django.utils import timezone
from dashboard.models import Doctor, Patient, Service, Appointment, MonthlyRevenue, ClinicSetting
from decimal import Decimal
import datetime


class Command(BaseCommand):
    help = 'Seeds database with realistic demo clinic data matching CareWell Clinic specifications'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE('Clearing existing clinic data...'))
        Appointment.objects.all().delete()
        Patient.objects.all().delete()
        Doctor.objects.all().delete()
        Service.objects.all().delete()
        MonthlyRevenue.objects.all().delete()
        ClinicSetting.objects.all().delete()

        self.stdout.write(self.style.NOTICE('Creating clinic settings...'))
        ClinicSetting.objects.create(
            clinic_name='CareWell Clinic',
            tagline='Healthcare Management Dashboard',
            currency_code='KES',
            admin_name='Admin',
            admin_role='Administrator'
        )

        self.stdout.write(self.style.NOTICE('Creating doctors...'))
        doctors_data = [
            ("Dr. Faith Muthoni", "Cardiology", "faith.muthoni@carewell.co.ke", "+254 712 345 678"),
            ("Dr. Brian Omondi", "Dental Surgery", "brian.omondi@carewell.co.ke", "+254 723 456 789"),
            ("Dr. Mercy Chebet", "Obstetrics & Gynecology", "mercy.chebet@carewell.co.ke", "+254 734 567 890"),
            ("Dr. Kevin Kiprop", "General Medicine", "kevin.kiprop@carewell.co.ke", "+254 745 678 901"),
            ("Dr. Jane Wambui", "Pediatrics", "jane.wambui@carewell.co.ke", "+254 756 789 012"),
            ("Dr. Dennis Otieno", "Pathology & Lab", "dennis.otieno@carewell.co.ke", "+254 767 890 123"),
            ("Dr. Collins Mwangi", "Orthopedics", "collins.mwangi@carewell.co.ke", "+254 778 901 234"),
            ("Dr. Esther Njeri", "Dermatology", "esther.njeri@carewell.co.ke", "+254 789 012 345"),
            ("Dr. Patrick Kimani", "ENT Specialist", "patrick.kimani@carewell.co.ke", "+254 790 123 456"),
            ("Dr. Sharon Achieng", "Internal Medicine", "sharon.achieng@carewell.co.ke", "+254 701 234 567"),
            ("Dr. Victor Njuguna", "Neurology", "victor.njuguna@carewell.co.ke", "+254 711 345 678"),
            ("Dr. Lucy Kerubo", "Family Medicine", "lucy.kerubo@carewell.co.ke", "+254 722 456 789"),
        ]

        doctors = []
        for name, spec, email, phone in doctors_data:
            doc = Doctor.objects.create(
                name=name,
                specialization=spec,
                email=email,
                phone=phone,
                is_active=True,
                joined_date=datetime.date(2026, 8, 1)
            )
            doctors.append(doc)

        self.stdout.write(self.style.NOTICE('Creating services...'))
        services_data = [
            ("General Checkup", "GEN-01", Decimal("2500.00"), "Comprehensive routine physical exam and health screening"),
            ("Dental Consultation", "DEN-01", Decimal("3500.00"), "Complete dental checkup, cleaning and consultation"),
            ("Dental Care", "DEN-02", Decimal("4500.00"), "Specialized dental procedures, hygiene and fillings"),
            ("Follow Up", "GEN-02", Decimal("1500.00"), "Post-treatment evaluation and medication adjustment"),
            ("Antenatal Care", "MAT-01", Decimal("3500.00"), "Maternal and fetal health monitoring during pregnancy"),
            ("Laboratory Test", "LAB-01", Decimal("1800.00"), "Diagnostic blood panel, urinalysis, and screening tests"),
            ("Child Health", "PED-01", Decimal("2000.00"), "Pediatric immunization, growth tracking and pediatric care"),
        ]

        services_dict = {}
        for name, code, price, desc in services_data:
            svc = Service.objects.create(name=name, code=code, price=price, description=desc, is_active=True)
            services_dict[name] = svc

        self.stdout.write(self.style.NOTICE('Creating patients...'))
        # Key patients
        p1 = Patient.objects.create(name="John Otieno", gender="Male", age=34, phone="+254 712 111 222", email="john.otieno@gmail.com")
        p2 = Patient.objects.create(name="Mary Akinyi", gender="Female", age=28, phone="+254 722 333 444", email="mary.akinyi@gmail.com")
        p3 = Patient.objects.create(name="Peter Mwangi", gender="Male", age=45, phone="+254 733 555 666", email="peter.mwangi@gmail.com")
        p4 = Patient.objects.create(name="Grace Wanjiku", gender="Female", age=29, phone="+254 744 777 888", email="grace.wanjiku@gmail.com")

        # Create bulk dummy patients to represent clinic patient registry
        extra_patients = []
        for i in range(5, 581):
            extra_patients.append(
                Patient(
                    name=f"Patient {i:03d}",
                    gender="Female" if i % 2 == 0 else "Male",
                    age=20 + (i % 55),
                    phone=f"+254 700 {i:03d} {(i*7)%900 + 100:03d}",
                    email=f"patient{i}@example.com",
                    created_at=timezone.now() - datetime.timedelta(days=i % 300)
                )
            )
        Patient.objects.bulk_create(extra_patients)

        self.stdout.write(self.style.NOTICE('Creating appointments for today (42 total)...'))
        today = datetime.date(2026, 8, 14)

        # 4 Recent Appointments exact matching
        Appointment.objects.create(
            patient=p1,
            doctor=doctors[3],
            service=services_dict["General Checkup"],
            date=today,
            time_str="09:00 AM",
            status="Confirmed"
        )
        Appointment.objects.create(
            patient=p2,
            doctor=doctors[1],
            service=services_dict["Dental Consultation"],
            date=today,
            time_str="10:00 AM",
            status="Completed"
        )
        Appointment.objects.create(
            patient=p3,
            doctor=doctors[3],
            service=services_dict["Follow Up"],
            date=today,
            time_str="11:00 AM",
            status="Pending"
        )
        Appointment.objects.create(
            patient=p4,
            doctor=doctors[2],
            service=services_dict["Antenatal Care"],
            date=today,
            time_str="02:00 PM",
            status="Confirmed"
        )

        # Remaining appointments breakdown to achieve:
        # Confirmed: 22 (we already have 2, need 20 more)
        # Completed: 12 (we already have 1, need 11 more)
        # Pending: 6 (we already have 1, need 5 more)
        # Cancelled: 2 (need 2)
        # Total = 42

        statuses_needed = (
            ['Confirmed'] * 20 +
            ['Completed'] * 11 +
            ['Pending'] * 5 +
            ['Cancelled'] * 2
        )

        services_pool = [
            services_dict["General Checkup"],
            services_dict["Dental Care"],
            services_dict["Antenatal Care"],
            services_dict["Laboratory Test"],
            services_dict["Child Health"],
        ]

        times_pool = [
            "08:30 AM", "09:15 AM", "09:45 AM", "10:30 AM", "11:15 AM", "11:45 AM",
            "12:15 PM", "12:45 PM", "01:15 PM", "01:45 PM", "02:30 PM", "03:00 PM",
            "03:30 PM", "04:00 PM", "04:30 PM", "05:00 PM", "05:30 PM", "06:00 PM"
        ]

        all_pts = list(Patient.objects.filter(id__gte=5)[:40])
        for idx, status in enumerate(statuses_needed):
            pt = all_pts[idx % len(all_pts)]
            svc = services_pool[idx % len(services_pool)]
            doc = doctors[idx % len(doctors)]
            t_str = times_pool[idx % len(times_pool)]
            Appointment.objects.create(
                patient=pt,
                doctor=doc,
                service=svc,
                date=today,
                time_str=t_str,
                status=status
            )

        self.stdout.write(self.style.NOTICE('Creating monthly revenue data...'))
        revenue_data = [
            ("Apr", 4, 2026, Decimal("85000.00"), False),
            ("May", 5, 2026, Decimal("100000.00"), False),
            ("Jun", 6, 2026, Decimal("102000.00"), False),
            ("Jul", 7, 2026, Decimal("120000.00"), False),
            ("Aug", 8, 2026, Decimal("125600.00"), True),
        ]
        for m_name, m_num, yr, amt, is_cur in revenue_data:
            MonthlyRevenue.objects.create(
                month_name=m_name,
                month_num=m_num,
                year=yr,
                amount=amt,
                is_current_month=is_cur
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded CareWell Clinic database!'))
