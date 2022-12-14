# Generated by Django 4.1.4 on 2023-01-08 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofiles_delete_profile'),
        ('test_generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GTest',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question_count', models.IntegerField()),
                ('answer_count', models.IntegerField()),
                ('test_score', models.FloatField(null=True)),
                ('test_time', models.TimeField(null=True)),
                ('last_answered_q', models.IntegerField(null=True)),
                ('done', models.BooleanField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='GTestAnswers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('correct', models.BooleanField()),
                ('done', models.BooleanField()),
                ('gtest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator.gtest')),
            ],
        ),
        migrations.CreateModel(
            name='TestAnswers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('letter_answer', models.CharField(max_length=10)),
                ('body_answer', models.JSONField()),
                ('correct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestions',
            fields=[
                ('tq_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question_num', models.IntegerField()),
                ('question_body', models.JSONField()),
                ('answer_count', models.SmallIntegerField()),
                ('owner_username_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('th_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('th_name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.RemoveField(
            model_name='test',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='test',
            name='theme',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.AddField(
            model_name='testquestions',
            name='th_name_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_generator.themes'),
        ),
        migrations.AddField(
            model_name='testanswers',
            name='question_num_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator.testquestions'),
        ),
        migrations.AddField(
            model_name='gtestanswers',
            name='letter_answer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator.testanswers'),
        ),
        migrations.AddField(
            model_name='gtestanswers',
            name='question_num_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator.testquestions'),
        ),
    ]
