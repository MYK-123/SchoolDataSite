from math import e
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest

from admissions import JsonSave
from .forms import (AdmissionFormForm, StudentDetailsForm, FatherDetailsForm, MotherDetailsForm,
                     GuardianDetailsForm, AddressDetailsForm, PreviousSchoolDetailsForm)

from .models import *

# Create your views here.

from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    AdmissionFormForm, StudentDetailsForm, FatherDetailsForm, MotherDetailsForm,
    GuardianDetailsForm, AddressDetailsForm, PreviousSchoolDetailsForm
)
from .models import AdmissionForm

class AdmissionManagementView(View):
    template_name = 'admissionFormTemplate.html'

    def get(self, request, enrolment_no=None):
        admission_instance = None
        if enrolment_no:
            admission_instance = get_object_or_404(AdmissionForm, enrolment_no=enrolment_no)

        context = {
            'admission_form': AdmissionFormForm(instance=admission_instance),
            'student_form': StudentDetailsForm(),
            'father_form': FatherDetailsForm(),
            'mother_form': MotherDetailsForm(),
            'guardian_form': GuardianDetailsForm(),
            'address_form': AddressDetailsForm(),
            'school_form': PreviousSchoolDetailsForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, enrolment_no=None):
        admission_instance = None
        student_instance = father_instance = mother_instance = guardian_instance = address_instance = school_instance = None
        if enrolment_no:
            admission_instance = get_object_or_404(AdmissionForm, enrolment_no=enrolment_no)
            student_instance = getattr(admission_instance, 'studentdetails', None)
            father_instance = FatherDetails.objects.filter(admission_form=admission_instance).first()
            mother_instance = MotherDetails.objects.filter(admission_form=admission_instance).first()
            guardian_instance = GuardianDetails.objects.filter(admission_form=admission_instance).first()
            address_instance = AddressDetails.objects.filter(admission_form=admission_instance).first()
            school_instance = PreviousSchoolDetails.objects.filter(admission_form=admission_instance).first()
        
        admission_form = AdmissionFormForm(request.POST, instance=admission_instance)
        student_form = StudentDetailsForm(request.POST, instance=student_instance)
        father_form = FatherDetailsForm(request.POST, instance=father_instance) 
        mother_form = MotherDetailsForm(request.POST, instance=mother_instance)
        guardian_form = GuardianDetailsForm(request.POST, instance=guardian_instance)
        address_form = AddressDetailsForm(request.POST, instance=address_instance)
        school_form = PreviousSchoolDetailsForm(request.POST, instance=school_instance)

        admission = None

        if admission_form.is_valid():
            admission = admission_form.save()
        
        if all([
            student_form.is_valid(),
            father_form.is_valid(), mother_form.is_valid(),
            address_form.is_valid(),
            school_form.is_valid()
        ]):
            for form in [student_form, father_form, mother_form,
                           address_form, school_form]:
                obj = form.save(commit=False)
                obj.admission_form = admission
                obj.save()
            if request.POST.get('addGuardian') == 'yes':
                if guardian_form.is_valid():
                    guardian = guardian_form.save(commit=False)
                    guardian.admission_form = admission
                    guardian.save()
            
            #return render(request, self.template_name, context)# redirect('success_url')  # Replace with your actual success URL/view name

        # If any form fails validation
        context = {
            'admission_form': admission_form,
            'student_form': student_form,
            'father_form': father_form,
            'mother_form': mother_form,
            'guardian_form': guardian_form,
            'address_form': address_form,
            'school_form': school_form,
        }

        return render(request, self.template_name, context)

def admission_form_view(request):
    if request.method == 'POST':
        form = AdmissionFormForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'admission_form.html', {'form': form})
        else:
            return render(request, 'admission_form.html', {'form': form})
    else:
        return render(request, 'admission_form.html', {'form': AdmissionFormForm()})

def admissionForm(request):
    return render(request=request, template_name='admissionFormTemplate.html')

def admissionFormSubmit(request : HttpRequest):
    if request.method == 'POST':
        return HttpResponse(content=request.POST.lists())
    reply = request.headers['User-Agent']
    return HttpResponse(content=reply)

