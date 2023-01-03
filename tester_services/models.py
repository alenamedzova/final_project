from django.db import models


# Create your models here.
class Theme(models.Model):
    theme_name = models.CharField(max_length=45)

    def __str__(self):
        return self.theme_name
