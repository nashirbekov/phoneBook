from django.db import models

# Create your models here.


class Phone(models.Model):
    """Телефон"""
    phonenumber = models.CharField("Номер", max_length=13)
    name = models.CharField("ФИО", max_length=100)
    city = models.CharField("Город", max_length=50)
    adress = models.CharField("Адрес", max_length=100)
    email = models.EmailField("Email")