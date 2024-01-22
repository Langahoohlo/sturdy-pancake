from django.db import models
from datetime import datetime

class  Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True) 

    def __str__(self):
        return self.email
