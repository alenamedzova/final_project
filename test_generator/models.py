from django.db import models
from django.utils.safestring import mark_safe

from profiles.models import *


# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=45, null=False)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    private = models.BooleanField(null=False, default=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    pass


class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    body_text = models.TextField(null=False)
    body_image = models.ImageField(null=False)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)
