from datetime import datetime
from django.db import models

# Create your models here.
class Donor_form(models.Model):
    email =models.CharField(max_length = 122)
    address1=models.CharField(max_length= 122)
    address2 = models.CharField(max_length = 122)
    district = models.CharField(max_length = 122)
    city = models.CharField(max_length = 122)
    state = models.CharField(max_length = 122)
    pincode = models.CharField(max_length = 122)
    contact_no =models.CharField(max_length = 12)
    size = models.CharField(max_length = 122)
    quantity = models.CharField(max_length = 122)
    date_s = models.CharField(max_length = 122)
    time = models.CharField(max_length = 122)
    e_img = models.FileField(upload_to='', storage=None, max_length=100)
    date = models.DateField()
    