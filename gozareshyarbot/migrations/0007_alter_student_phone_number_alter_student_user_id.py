# Generated by Django 4.0.4 on 2022-05-27 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gozareshyarbot', '0006_alter_student_phone_number_alter_student_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='user_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
