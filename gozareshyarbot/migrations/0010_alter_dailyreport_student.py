# Generated by Django 4.0.4 on 2022-05-27 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gozareshyarbot', '0009_alter_dailyreport_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gozareshyarbot.student'),
        ),
    ]