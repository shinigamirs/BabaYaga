from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(primary_key=True, max_length=10)
    fine_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
