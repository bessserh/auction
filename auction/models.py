from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Photo(models.Model):
    photo = models.ImageField()

    def __str__(self):
        return self.photo.url


class Item(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    date_stop = models.DateTimeField(blank=True) # атрибуты что добавить
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LotWin(models.Model):
    bet = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.bet} {self.item.name} {self.item.price}'



