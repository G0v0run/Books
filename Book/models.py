from django.db import models
from django.utils import timezone

# Create your models here.

class Sheets(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    compositors = models.CharField(max_length=200)
    available = models.BooleanField()
    price = models.IntegerField()

    class Meta:
        db_table = 'sheets'

class SheetImage(models.Model):
    image = models.ImageField()
    sheet = models.ForeignKey(Sheets, on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'sheet_images'
    

class Buyers(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    sheets = models.ForeignKey(Sheets, on_delete=models.CASCADE)

    class Meta:
        db_table = 'buyers'

class Order(models.Model):
    DELIVERY_CHOICES = [
        ('NP', 'Новая Почта'),
        ('UP', 'Укр почта'),
    ]

    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    sheet = models.ForeignKey(Sheets, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    delivery = models.CharField(max_length=2, choices=DELIVERY_CHOICES)
    phone = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200, blank=True)
    additional = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'orders'