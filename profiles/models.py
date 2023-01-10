from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.FloatField(null=True)
    last_done_test = models.DateField(null=True)
    test_count = models.IntegerField(null=True)

    first_name_private = models.BooleanField(default=False, null=False)
    last_name_private = models.BooleanField(default=False, null=False)
    email_private = models.BooleanField(default=False, null=False)
    score_private = models.BooleanField(default=False, null=False)
    last_done_test_private = models.BooleanField(default=False, null=False)
    test_count_private = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.user.username


# create profile when register
def registration_create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfiles(user=instance)
        user_profile.save()


post_save.connect(registration_create_profile, sender=User)
