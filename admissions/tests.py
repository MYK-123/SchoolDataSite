from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import (
    AdmissionForm, StudentDetails, FatherDetails, MotherDetails,
    GuardianDetails, AddressDetails, PreviousSchoolDetails
)

import os
import json
from django.test import TestCase
from django.utils.timezone import now

from .JsonSave import *  # adjust import to match your file


class AdmissionFormPostTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_admission')
        self.valid_post_data = {
            # AdmissionForm
            'declaration': True,
            'admission_date': '2024-06-01',

            # StudentDetails
            'student_name': 'Test Student',
            'student_class': '10',
            'student_aadhar': '123456789012',
            'student_date_of_birth': '2008-05-01',
            'student_religion': 'Hindu',
            'student_nationality': 'Indian',
            'student_category': 'General',
            'student_category_other': '',
            'student_gender': 'Male',
            'student_blood_group': 'A+',
            'student_height': '170',
            'student_weight': '60',
            'student_disability': 'None',
            'student_facility': 'No',
            'student_email': 'student@example.com',
            'student_whatsapp': '9876543210',

            # FatherDetails
            'father_name': 'John Doe',
            'father_id': 'PAN',
            'father_id_number': 'ABCDE1234F',
            'father_occupation': 'Engineer',
            'father_qualification': 'B.Tech',
            'father_aadhar': '123456789012',
            'father_mobile': '9876543210',

            # MotherDetails
            'mother_name': 'Jane Doe',
            'mother_id': 'PAN',
            'mother_id_number': 'ABCDE4321F',
            'mother_occupation': 'Teacher',
            'mother_qualification': 'M.A.',
            'mother_aadhar': '123456789013',
            'mother_mobile': '9876543211',

            # GuardianDetails
            'addGuardian': 'yes',
            'guardian_name': 'Uncle Doe',
            'guardian_id': 'PAN',
            'guardian_id_number': 'ABCDE5678F',
            'guardian_occupation': 'Lawyer',
            'guardian_qualification': 'LLB',
            'guardian_aadhar': '123456789014',
            'guardian_mobile': '9876543212',

            # AddressDetails
            'address': '123 Main St',
            'city': 'Delhi',
            'state': 'Delhi',
            'pincode': '110001',
            'landmark': 'Near Park',
            'distance_from_school': '2.5',

            # PreviousSchoolDetails
            'prev_school_name': 'ABC School',
            'from_class': '8',
            'to_class': '9',
            'from_year': 2022,
            'to_year': 2023,
        }

    def test_admission_form_submission(self):
        response = self.client.post(self.url, self.valid_post_data)
        self.assertEqual(response.status_code, 200)

        # Check if AdmissionForm and StudentDetails were created
        admission_exists = AdmissionForm.objects.exists()
        student_exists = StudentDetails.objects.exists()

        self.assertTrue(admission_exists, "AdmissionForm should be created")
        self.assertTrue(student_exists, "StudentDetails should be created")

        # Optionally check generated enrolment_no
        admission = AdmissionForm.objects.first()
        self.assertTrue(admission.enrolment_no.startswith("ZMS"), "Autogen enrolment number should be set")





class JsonExportTestCase(TestCase):
    def setUp(self):
        self.admission = AdmissionForm.objects.create(
            pen_no="PEN001",
            aapar_id="AAP001",
            file_no="F001",
            admission_date=now().date(),
            declaration=True
        )
        self.admission.enrolment_no = f"ZMS{self.admission.admission_date.strftime('%Y%m%d')}_{self.admission.student_id}"
        self.admission.save()

        StudentDetails.objects.create(
            admission_form=self.admission,
            student_name="Jane Doe",
            student_class="9",
            student_aadhar="111122223333",
            student_date_of_birth="2010-05-01",
            student_religion="Hindu",
            student_nationality="Indian",
            student_category="General",
            student_category_other="",
            student_gender="Female",
            student_blood_group="B+",
            student_height="155cm",
            student_weight="45kg",
            student_disability="None",
            student_facility="No",
            student_email="jane@example.com",
            student_whatsapp="9876543210"
        )

        FatherDetails.objects.create(
            admission_form=self.admission,
            father_name="John Doe",
            father_id="FID001",
            father_id_number="12345",
            father_occupation="Engineer",
            father_qualification="B.Tech",
            father_aadhar="444455556666",
            father_mobile="9998887776"
        )

        MotherDetails.objects.create(
            admission_form=self.admission,
            mother_name="Mary Doe",
            mother_id="MID001",
            mother_id_number="54321",
            mother_occupation="Teacher",
            mother_qualification="M.Sc",
            mother_aadhar="777788889999",
            mother_mobile="8887776665"
        )

        GuardianDetails.objects.create(
            admission_form=self.admission,
            guardian_name="Guardian One",
            guardian_id="GID001",
            guardian_id_number="G123456",
            guardian_occupation="Doctor",
            guardian_qualification="MBBS",
            guardian_aadhar="111133334444",
            guardian_mobile="7776665554"
        )

        AddressDetails.objects.create(
            admission_form=self.admission,
            address="123 School St",
            city="EduCity",
            state="Knowledge",
            pincode="123456",
            landmark="Next to Library",
            distance_from_school=1.5
        )

        PreviousSchoolDetails.objects.create(
            admission_form=self.admission,
            prev_school_name="Old School",
            from_class="7",
            to_class="8",
            from_year=2019,
            to_year=2020
        )

    def test_json_export(self):
        exporter = JsonSave()
        exporter.handle(enrolment_no=self.admission.enrolment_no)

        # Verify file created
        self.assertTrue(os.path.exists('data.json'))

        # Load and verify contents
        with open('data.json', 'r') as f:
            data = json.load(f)

            self.assertEqual(len(data), 1)
            exported = data[0]

            self.assertEqual(exported['enrolment_no'], self.admission.enrolment_no)
            self.assertEqual(exported['student_details']['student_name'], "Jane Doe")
            self.assertEqual(exported['father_details']['father_name'], "John Doe")

        # Clean up
        os.remove('data.json')
        self.assertFalse(os.path.exists('data.json'))
