import json

from django.shortcuts import get_object_or_404
from .models import AdmissionForm, StudentDetails, FatherDetails, MotherDetails, GuardianDetails, AddressDetails, PreviousSchoolDetails

class JsonSave():
    help = 'Save model data to JSON file'

    def handle(self,enrolment_no=None):
        # Initialize an empty list to store all the data
        all_data = []

        if enrolment_no:
            admission_instance = get_object_or_404(AdmissionForm, enrolment_no=enrolment_no)

        # Query all data from the models
        admission_forms = AdmissionForm.objects.filter(enrolment_no=enrolment_no) if enrolment_no else AdmissionForm.objects.all()

        for admission in admission_forms:
            admission_data = {
                'student_id': admission.student_id,
                'enrolment_no': admission.enrolment_no,
                'pen_no': admission.pen_no,
                'aapar_id': admission.aapar_id,
                'file_no': admission.file_no,
                'admission_date': admission.admission_date.strftime('%Y-%m-%d'),
                'declaration': admission.declaration,
            }

            # Fetch related data for StudentDetails
            student_details = StudentDetails.objects.get(admission_form=admission)
            admission_data['student_details'] = {
                'student_name': student_details.student_name,
                'student_class': student_details.student_class,
                'student_aadhar': student_details.student_aadhar,
                'student_date_of_birth': student_details.student_date_of_birth.strftime('%Y-%m-%d'),
                'student_religion': student_details.student_religion,
                'student_nationality': student_details.student_nationality,
                'student_category': student_details.student_category,
                'student_category_other': student_details.student_category_other,
                'student_gender': student_details.student_gender,
                'student_blood_group': student_details.student_blood_group,
                'student_height': student_details.student_height,
                'student_weight': student_details.student_weight,
                'student_disability': student_details.student_disability,
                'student_facility': student_details.student_facility,
                'student_email': student_details.student_email,
                'student_whatsapp': student_details.student_whatsapp,
            }

            # FatherDetails
            father_details = FatherDetails.objects.get(admission_form=admission)
            admission_data['father_details'] = {
                'father_name': father_details.father_name,
                'father_id': father_details.father_id,
                'father_id_number': father_details.father_id_number,
                'father_occupation': father_details.father_occupation,
                'father_qualification': father_details.father_qualification,
                'father_aadhar': father_details.father_aadhar,
                'father_mobile': father_details.father_mobile,
            }

            # MotherDetails
            mother_details = MotherDetails.objects.get(admission_form=admission)
            admission_data['mother_details'] = {
                'mother_name': mother_details.mother_name,
                'mother_id': mother_details.mother_id,
                'mother_id_number': mother_details.mother_id_number,
                'mother_occupation': mother_details.mother_occupation,
                'mother_qualification': mother_details.mother_qualification,
                'mother_aadhar': mother_details.mother_aadhar,
                'mother_mobile': mother_details.mother_mobile,
            }

            # GuardianDetails
            guardian_details = GuardianDetails.objects.get(admission_form=admission)
            admission_data['guardian_details'] = {
                'guardian_name': guardian_details.guardian_name,
                'guardian_id': guardian_details.guardian_id,
                'guardian_id_number': guardian_details.guardian_id_number,
                'guardian_occupation': guardian_details.guardian_occupation,
                'guardian_qualification': guardian_details.guardian_qualification,
                'guardian_aadhar': guardian_details.guardian_aadhar,
                'guardian_mobile': guardian_details.guardian_mobile,
            }

            # AddressDetails
            address_details = AddressDetails.objects.get(admission_form=admission)
            admission_data['address_details'] = {
                'address': address_details.address,
                'city': address_details.city,
                'state': address_details.state,
                'pincode': address_details.pincode,
                'landmark': address_details.landmark,
                'distance_from_school': address_details.distance_from_school,
            }

            # PreviousSchoolDetails
            prev_school_details = PreviousSchoolDetails.objects.get(admission_form=admission)
            admission_data['previous_school_details'] = {
                'prev_school_name': prev_school_details.prev_school_name,
                'from_class': prev_school_details.from_class,
                'to_class': prev_school_details.to_class,
                'from_year': prev_school_details.from_year,
                'to_year': prev_school_details.to_year,
            }

            # Append the admission data to the all_data list
            all_data.append(admission_data)

        # Write the data to a JSON file
        with open('data.json', 'w') as json_file:
            json.dump(all_data, json_file, indent=4)

        print('Successfully saved data to JSON')
