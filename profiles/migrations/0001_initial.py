# Generated by Django 4.1.4 on 2023-01-03 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('about_me', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('score', models.FloatField(null=True)),
                ('last_done_test', models.DateField(null=True)),
                ('test_count', models.IntegerField(null=True)),
                ('first_name_private', models.BooleanField(default=False)),
                ('last_name_private', models.BooleanField(default=False)),
                ('about_me_private', models.BooleanField(default=False)),
                ('email_private', models.BooleanField(default=False)),
                ('birth_date_private', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]