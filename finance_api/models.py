from django.db import models

class ContactInfo(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    email = models.EmailField(('email address'), blank=True, null=True)
    full_address = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=20, blank=True, null=True)
    occupation = models.CharField(max_length=20)
    monthly_income = models.CharField(max_length=20)
    asset_type = models.CharField(max_length=50)
    contact_status_id = models.CharField(max_length=20)
    lifecycle_stage_id= models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.first_name