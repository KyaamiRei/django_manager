from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.IntegerField(blank=False, verbose_name="пользователь")
    user_email = models.CharField(max_length=254, verbose_name="email пользователя")
    user_balance = models.FloatField(default=0, verbose_name="баланс пользователя")

    def __str__(self):
        return self.user_email


class Transaction(models.Model):
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE)
    price = models.FloatField(blank=False, verbose_name="цена")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="категория")
    description = models.TextField(blank=True, verbose_name="описание")

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(max_length=45, db_index=True, verbose_name="категория")

    def __str__(self):
        return self.name
