from django.db import models

# Create your models here.
class Student(models.Model):
    user_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName

class DailyReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    wakeUpTime = models.CharField(max_length=10)
    sleepTime = models.CharField(max_length=10)


class StudyTask(models.Model):
    dailyReport = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    subject = models.CharField(max_length=40)
    time = models.CharField(max_length=10)
    numberOfTest = models.IntegerField()
    qualityOfStudy = models.IntegerField()


    