from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor

class Listings(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class HomeType(models.TextChoices):
        STANDALONEHOUSE = 'Stand Alone House'
        DUPLEX = 'Duplex'
        BACHELOR = 'Bachelor'


    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=10, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField(max_length=10, default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    home_type = models.CharField(max_length=100, choices=HomeType.choices, blank=True)
    sqm = models.IntegerField(default=0)
    open_house = models.BooleanField(default=False)
    display_photo = models.ImageField(upload_to='listings/%Y/%m/%d/')
    list_photo_1 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_2 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_3 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_4 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_5 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_6 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_7 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_8 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_9 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_10 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    list_photo_12 = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title