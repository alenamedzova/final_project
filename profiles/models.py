from django.db import models
from django.contrib.auth.models import User


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
