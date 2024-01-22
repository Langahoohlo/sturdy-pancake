from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='realtors/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name