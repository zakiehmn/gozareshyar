from .models import Student, DailyReport, StudyTask
from datetime import date

def get_student(user_id):
    student = Student.objects.filter(user_id=user_id).last()
    return student

def get_daily_report_student(user_id):
    student = get_student(user_id)
    daily_report = DailyReport.objects.filter(student=student).last()
    return daily_report

def get_study_task_report(report):
    study_task = StudyTask.objects.filter(daily_report=report).last()
    return study_task



def get_student_profile_text(user_id):
    student = get_student(user_id)
    fist_name = student.first_name
    last_name = student.last_name
    phone_number = student.phone_number
    grade = student.grade
    student_profile_text = "اطلاعاتت:\n نام:{} \n نام خانوادگی:{} \n شماره تلفن:{} \n پایه تحصیلی:{} \n ".format(fist_name, last_name, phone_number, grade)
    return student_profile_text

def set_wake_up_time(user_id, time):
    student = get_student(user_id)
    daily_report = get_daily_report_student(user_id)
    daily_report = DailyReport.objects.filter(student=student).update(wake_up_time=time)

def set_subject(user_id, subject):
    daily_report = get_daily_report_student(user_id)
    # study_task = create_study_task(user_id)
    # study_task = StudyTask.objects.filter(daily_report=daily_report).update(subject=subject)
    study_task = StudyTask.objects.create(daily_report=daily_report, subject=subject)


def set_time(user_id, time):
    daily_report = get_daily_report_student(user_id)
    study_task = StudyTask.objects.filter(daily_report=daily_report).last()
    study_task.time = time
    study_task.save()


def delete_study_task(user_id):
    daily_report = get_daily_report_student(user_id)
    study_task = StudyTask.objects.get(daily_report=daily_report).delete()

# def set_time_null(user_id):
#     student = get_student(user_id)
#     daily_report = get_daily_report_student(student)
#     study_task = StudyTask.objects.filter(daily_report=daily_report).update(time=time)

def create_daily_report(user_id):
    student = get_student(user_id)
    date_now = date.today()
    print(date_now)
    try:
        daily_report = DailyReport.objects.get_or_create(student=student, date=date_now)
    except:
        pass

def set_test_number(user_id, test_num):
    daily_report = get_daily_report_student(user_id)
    study_task = StudyTask.objects.filter(daily_report=daily_report).last()
    study_task.number_of_test = test_num
    study_task.save()

def set_quality_study(user_id, quality_num):
    daily_report = get_daily_report_student(user_id)
    study_task = StudyTask.objects.filter(daily_report=daily_report).last()
    study_task.quality_of_study = quality_num
    study_task.save()

def exist_report_today(user_id):
    daily_report = get_daily_report_student(user_id)
    date_now = date.today()
    if daily_report.date == date_now:
        print("false")
        return False
    