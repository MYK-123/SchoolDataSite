# Add URL maps to redirect the base URL to our application

from django.urls import path
from . import views
from .views import AdmissionManagementView

urlpatterns = [
    path('admission_form', views.admission_form_view, name='admission_form'),  # URL for the admission form view
    path('admissionForm', views.admissionForm, name='admissionForm'),
    path('admissionFormSubmit', views.admissionFormSubmit, name='admissionFormSubmit'),
    
    path('', AdmissionManagementView.as_view(), name='create_admission'),
    path('admission', AdmissionManagementView.as_view(), name='create_admission'),
    path('admission/<str:enrolment_no>', AdmissionManagementView.as_view(), name='edit_admission'),
]
