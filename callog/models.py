from django.db import models
from django.utils import timezone


class WeighIn(models.Model):
    date = models.DateField(default=timezone.now)
    pounds = models.FloatField(default=0)
