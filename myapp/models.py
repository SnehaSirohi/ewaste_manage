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
    date_s = models.CharField(max_length = 122)
    time = models.CharField(max_length = 122)
    ename = models.CharField(max_length=122)
    quantity = models.CharField(max_length=122)
    EwasteType = models.CharField(max_length=122)
    size = models.CharField(max_length = 122)
    weight = models.CharField(max_length=122)
    e_img1 = models.FileField(upload_to='', storage=None, max_length=100)
    e_img2 = models.FileField(upload_to='', storage=None, max_length=100)
    e_img3 = models.FileField(upload_to='',storage=None, max_length=100)
    date = models.DateField()
    