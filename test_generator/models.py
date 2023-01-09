from django.db import models
from django.utils.safestring import mark_safe

from profiles.models import *


# Create your models here.
class Themes(models.Model):
    th_id = models.BigAutoField(primary_key=True)
    th_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.th_name


class TestQuestions(models.Model):
    tq_id = models.BigAutoField(primary_key=True)
    question_num = models.IntegerField(null=False)
    question_body = models.JSONField(null=False)
    answer_count = models.SmallIntegerField(null=False)
    th_name_id = models.ForeignKey(Themes, on_delete=models.SET_NULL, null=True)
    owner_username_id = models.ForeignKey(UserProfiles, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tq_id


class TestAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_num_id = models.ForeignKey(TestQuestions, on_delete=models.CASCADE, null=False)
    letter_answer = models.CharField(max_length=10, null=False)
    body_answer = models.JSONField(null=False)
    correct = models.BooleanField(null=False)

    def __str__(self):
        return self.id


class GTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfiles, on_delete=models.SET_NULL, null=True)
    question_count = models.IntegerField(null=False)
    answer_count = models.IntegerField(null=False)
    test_score = models.FloatField(null=True)
    test_time = models.TimeField(null=True)
    last_answered_q = models.IntegerField(null=True)
    done = models.BooleanField(null=False)

    th_name_id = models.IntegerField(null=False)  # aby sme vedeli potom triediť otázky

    def __str__(self):
        return self.id


class GTestAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    gtest_id = models.ForeignKey(GTest, on_delete=models.CASCADE, null=False)
    question_num_id = models.ForeignKey(TestQuestions, on_delete=models.CASCADE, null=False)
    letter_answer_id = models.ForeignKey(TestAnswers, on_delete=models.CASCADE, null=False)
    correct = models.BooleanField(null=False)
    done = models.BooleanField(null=False)

    def __str__(self):
        return self.id
