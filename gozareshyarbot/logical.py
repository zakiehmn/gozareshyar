from .models import Student, DailyReport, StudyTask

def get_student(user_id):
    student = Student.objects.filter(user_id=user_id).last()
    return student

def get_daily_report_student(student):
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
    student = get_student(user_id)
    print(student)
    daily_report = get_daily_report_student(student)
    print(daily_report)
    study_task = create_study_task(user_id)
    print(study_task)
    # study_task = get_study_task_report(daily_report)
    study_task = StudyTask.objects.filter(daily_report=daily_report).update(subject=subject)

def create_study_task(user_id):
    student = get_student(user_id)
    daily_report = get_daily_report_student(student)
    study_task = StudyTask(daily_report=daily_report)
    study_task.save()
    return study_task
