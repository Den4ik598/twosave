from django.db import models

# Create your models here.
class Food(models.Model):
    Name_Currency = models.CharField('Выберните валюту',max_length=100)
    Curs_BANK = models.FloatField()
    Kurs_sell = models.FloatField()
    Kurs_buy = models.FloatField()
    number_of_currency = models.IntegerField()


class Payment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
