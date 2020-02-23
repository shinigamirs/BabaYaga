from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class UserProfile(User):
    employee_id = models.CharField(primary_key=True, max_length=10)
    fine_amount = models.IntegerField(default=0)

