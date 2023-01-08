from django.contrib import admin
from test_generator.models import *

# Register your models here.
admin.site.register(Themes)
admin.site.register(TestQuestions)
admin.site.register(TestAnswers)
admin.site.register(GTest)
admin.site.register(GTestAnswers)