from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class WeighIn(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(default=timezone.now, unique=True)
    pounds = models.FloatField(default=0)
