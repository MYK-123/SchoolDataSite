from turtle import rt
from django import forms
from .models import (
    AdmissionForm, StudentDetails, FatherDetails, MotherDetails,
    GuardianDetails, AddressDetails, PreviousSchoolDetails
)

class AdmissionFormForm(forms.ModelForm):
    class Meta:
        model = AdmissionForm
        exclude=['enrolment_no_autogen']
    
    def is_valid(self):
        v = super().is_valid()
        if not v:
            for field in self.errors.items():
                print(f"Field: {field[0]}, Error: {field[1]}")
        return v

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        exclude=['admission_form']
    
    def is_valid(self):
        v = super().is_valid()
        if not v:
            for field in self.errors.items():
                print(f"Field: {field[0]}, Error: {field[1]}")
        return v

class FatherDetailsForm(forms.ModelForm):
    class Meta:
        model = FatherDetails
        exclude=['admission_form']
    
    def is_valid(self):
        v = super().is_valid()
        if not v:
            for field in self.errors.items():
                print(f"Field: {field[0]}, Error: {field[1]}")
        return v

class MotherDetailsForm(forms.ModelForm):
    class Meta:
        model = MotherDetails
        exclude=['admission_form']
    
    def is_valid(self):
        v = super().is_valid()
        if not v:
            for field in self.errors.items():
                print(f"Field: {field[0]}, Error: {field[1]}")
        return v

class GuardianDetailsForm(forms.ModelForm):
    class Meta:
        model = GuardianDetails
        exclude=['admission_form']
    
    def is_valid(self):
        v = super().is_valid()
        if not v:
            for field in self.errors.items():
                print(f"Field: {field[0]}, Error: {field[1]}")
        return v

class AddressDetailsForm(forms.ModelForm):
    class Meta:
        model = AddressDetails
        exclude=['admission_form']
    
    def is_valid(self):
        v = super().is_valid()
        if not v:
            for field in self.errors.items():
                print(f"Field: {field[0]}, Error: {field[1]}")
        return v

class PreviousSchoolDetailsForm(forms.ModelForm):
    class Meta:
        model = PreviousSchoolDetails
        exclude=['admission_form']
    
    def is_valid(self):
        v = super().is_valid()
        if not v:
            for field in self.errors.items():
                print(f"Field: {field[0]}, Error: {field[1]}")
        return v
