# Generated by Django 4.1.4 on 2023-01-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_generator', '0002_gtest_gtestanswers_testanswers_testquestions_themes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gtest',
            name='th_name_id',
            field=models.IntegerField(null=True),
        ),
    ]
