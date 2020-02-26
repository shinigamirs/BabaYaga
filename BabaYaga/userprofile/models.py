from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from social_django.models import UserSocialAuth

from userprofile.fetchdata import *


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(primary_key=True, max_length=10)
    fine_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            profile = UserProfile.objects.get(user=instance)
            return 0
        except ObjectDoesNotExist:
            try:

                user_social = UserSocialAuth.objects.get(user=instance)
                token = user_social.extra_data.get("access_token")
                data = fetchdata(token)

                try:
                    profile = UserProfile.objects.get(employee_id=data.get("employee_id").lower())
                    old_user = profile.user
                    profile.user = instance
                    profile.save()
                    old_user.delete()
                    return 0

                except Exception:
                    profile = UserProfile()
                    profile.user = instance
                    profile.employee_id = data.get("employee_id").lower()
                    profile.save()

            except ObjectDoesNotExist:
                pass