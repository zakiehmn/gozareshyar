# Generated by Django 4.0.4 on 2022-05-25 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gozareshyarbot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studytask',
            name='dailyReport',
        ),
        migrations.RemoveField(
            model_name='studytask',
            name='subject',
        ),
        migrations.DeleteModel(
            name='DailyReport',
        ),
        migrations.DeleteModel(
            name='StudyTask',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]