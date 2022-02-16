from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True,
                                      default=18)
