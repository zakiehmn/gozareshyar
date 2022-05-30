from django.db import models

# Create your models here.
class Student(models.Model):
    user_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class DailyReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    wake_up_time = models.CharField(max_length=10)
    sleep_time = models.CharField(max_length=10)


class StudyTask(models.Model):
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    subject = models.CharField(max_length=40)
    time = models.CharField(max_length=20)
    number_of_test = models.IntegerField(null=True)
    quality_of_study = models.IntegerField(null=True)
