from django.contrib import admin

# Register your models here.
from .models import AdmissionForm, StudentDetails, FatherDetails, MotherDetails, GuardianDetails, AddressDetails,PreviousSchoolDetails

admin.register(AdmissionForm)
admin.register(StudentDetails)
admin.register(FatherDetails)
admin.register(MotherDetails)
admin.register(GuardianDetails)
admin.register(AddressDetails)
admin.register(PreviousSchoolDetails)

