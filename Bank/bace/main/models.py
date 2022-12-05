from django.db import models

# Create your models here.
class Food(models.Model):
    Name_Currency = models.CharField('Выберните валюту',max_length=100)
    Curs_BANK = models.FloatField()
    Kurs_sell = models.FloatField()
    Kurs_buy = models.FloatField()
    number_of_currency = models.IntegerField()
    Date = models.CharField(max_length=100,null=True)


class Payment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

class Number(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=10, blank=False, null=True)
    number = models.PositiveIntegerField(blank=False, null=True)
    phone = models.IntegerField()
    Inn = models.IntegerField()

    def __str__(self):
        return self.username


