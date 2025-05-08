import django
from django.db import models
from django.db.models import F
import django.utils
import django.utils.timezone

# Create your models here.

class AdmissionForm(models.Model):
    student_id = models.AutoField(primary_key=True)
    enrolment_no = models.CharField(max_length=20, unique=True, null=True, blank=True)
    pen_no = models.CharField(max_length=20, blank=True)
    aapar_id = models.CharField(max_length=20, blank=True)
    file_no = models.CharField(max_length=20, blank=True)
    admission_date = models.DateField(default=django.utils.timezone.now, blank=True)
    declaration = models.BooleanField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.enrolment_no and self.admission_date and self.student_id:
            self.enrolment_no = f"ZMS{self.admission_date.strftime('%Y%m%d')}_{self.student_id}"
            super().save(update_fields=['enrolment_no'])
            print(f'Enrolment No: {self.enrolment_no}')

    def __str__(self):
        return self.enrolment_no


class StudentDetails(models.Model):
    admission_form = models.OneToOneField(AdmissionForm, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=60)
    student_class = models.CharField(max_length=8)
    student_aadhar = models.CharField(max_length=12)
    student_date_of_birth = models.DateField()
    student_religion = models.CharField(max_length=15)
    student_nationality = models.CharField(max_length=15)
    student_category = models.CharField(max_length=10)
    student_category_other = models.CharField(max_length=20, blank=True)
    student_gender = models.CharField(max_length=6)
    student_blood_group = models.CharField(max_length=3)
    student_height = models.CharField(max_length=10)
    student_weight = models.CharField(max_length=10)
    student_disability = models.CharField(max_length=50, default='None')
    student_facility = models.CharField(max_length=50, default='No')
    student_email = models.EmailField()
    student_whatsapp = models.CharField(max_length=10)
    #student_image = models.ImageField(upload_to='student_images/', default='default.jpg', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Saving {self.__str__()} in DB')

    def __str__(self):
        return self.student_name


class FatherDetails(models.Model):
    admission_form = models.ForeignKey(AdmissionForm, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=60)
    father_id = models.CharField(max_length=20)
    father_id_number = models.CharField(max_length=20)
    father_occupation = models.CharField(max_length=20)
    father_qualification = models.CharField(max_length=15)
    father_aadhar = models.CharField(max_length=12)
    father_mobile = models.CharField(max_length=10)
    #father_image = models.ImageField(upload_to='father_images/', default='default.jpg', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Saving {self.__str__()} in DB')

    def __str__(self):
        return self.father_name


class MotherDetails(models.Model):
    admission_form = models.ForeignKey(AdmissionForm, on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=60)
    mother_id = models.CharField(max_length=20)
    mother_id_number = models.CharField(max_length=20)
    mother_occupation = models.CharField(max_length=20)
    mother_qualification = models.CharField(max_length=15)
    mother_aadhar = models.CharField(max_length=12)
    mother_mobile = models.CharField(max_length=10)
    #mother_image = models.ImageField(upload_to='mother_images/', default='default.jpg', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Saving {self.__str__()} in DB')
    
    def __str__(self):
        return self.mother_name


class GuardianDetails(models.Model):
    admission_form = models.ForeignKey(AdmissionForm, on_delete=models.CASCADE)
    guardian_name = models.CharField(max_length=60)
    guardian_id = models.CharField(max_length=20)
    guardian_id_number = models.CharField(max_length=20)
    guardian_occupation = models.CharField(max_length=20)
    guardian_qualification = models.CharField(max_length=15)
    guardian_aadhar = models.CharField(max_length=12)
    guardian_mobile = models.CharField(max_length=10)
    #guardian_image = models.ImageField(upload_to='guardian_images/', default='default.jpg', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Saving {self.__str__()} in DB')

    def __str__(self):
        return self.guardian_name


class AddressDetails(models.Model):
    admission_form = models.ForeignKey(AdmissionForm, on_delete=models.CASCADE)
    address = models.TextField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    landmark = models.CharField(max_length=20)
    distance_from_school = models.FloatField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Saving {self.__str__()} in DB')

    def __str__(self):
        return self.address


class PreviousSchoolDetails(models.Model):
    admission_form = models.ForeignKey(AdmissionForm, on_delete=models.CASCADE)
    prev_school_name = models.CharField(max_length=60)
    from_class = models.CharField(max_length=10)
    to_class = models.CharField(max_length=10)
    from_year = models.IntegerField()
    to_year = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Saving {self.__str__()} in DB')

    def __str__(self):
        return self.prev_school_name
