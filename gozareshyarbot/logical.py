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
    study_task = StudyTask.objects.filter(daily_report=daily_report).last()
    study_task.delete()

# def set_time_null(user_id):
#     student = get_student(user_id)
#     daily_report = get_daily_report_student(student)
#     study_task = StudyTask.objects.filter(daily_report=daily_report).update(time=time)

def create_daily_report(user_id):
    student = get_student(user_id)
    print(student)
    # date_now = date.today()
    # print(date_now)
    daily_report = DailyReport.objects.create(student=student)
    daily_report.save()
    return daily_report


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
    if daily_report is not None:
        if daily_report.date == date_now:
            return True
        return False
    return False

def set_date_report(user_id):
    daily_report =get_daily_report_student(user_id)
    student = get_student(user_id)
    date_now = date.today()
    daily_report = DailyReport.objects.filter(student=student).update(date=date_now)

def set_sleep_time(user_id, time):
    student = get_student(user_id)
    daily_report = get_daily_report_student(user_id)
    daily_report = DailyReport.objects.filter(student=student).update(sleep_time=time)
    
def get_report_text(user_id):
    student = get_student(user_id)
    daily_report = get_daily_report_student(user_id)
    first_name = student.first_name
    grade = student.grade
    date = daily_report.date
    wake_up_time = daily_report.wake_up_time
    sleep_time = daily_report.sleep_time
    tasks_texts = tasks_text(daily_report)
    sum_minutes = get_sum_minutes_task(daily_report)
    sum_test = get_sum_test_task(daily_report)
    text = "نام : {} \n تاریخ گزارش : {} \n پایه تحصیلی : {} \n پارت های مطالعاتی : {} \n وقت بیداری : {} \n وقت خواب : {} \n مجموع دقایق : {} \n مجموع تست ها : {} \n".format(first_name, date, grade, tasks_texts, wake_up_time, sleep_time, sum_minutes, sum_test)
    return str(text)




def get_task_text(study_task):
    subject = study_task.subject
    time = study_task.time
    number_of_test = study_task.number_of_test
    quality_of_study = study_task.quality_of_study
    emoji = quality_emoji(quality_of_study)
    text = "{} : {} | {} | {} ".format(subject, time, number_of_test, emoji)
    return str(text)

def quality_emoji(quality):
    emoji = ""
    if quality == 5:
        emoji = "😎"
    elif quality == 4:
        emoji = "😍"
    elif quality == 3:
        emoji = "🤩"
    elif quality == 2:
        emoji = "🙂"
    elif quality == 1:
        emoji = "😑"
    return emoji


def get_sum_minutes_task(daily_report):
    study_task = StudyTask.objects.filter(daily_report=daily_report)
    sum = 0
    for task in study_task:
        sum += int(task.time)
    return sum

def get_sum_test_task(daily_report):
    study_task = StudyTask.objects.filter(daily_report=daily_report)
    sum = 0
    for task in study_task:
        if task.number_of_test is not None:
            sum += task.number_of_test
    return sum

def tasks_text(daily_report):
    study_tasks = StudyTask.objects.filter(daily_report=daily_report)
    output_text = ""
    for task in study_tasks:
        output_text += str(get_task_text(task))+"\n"
    return str(output_text)

def set_message_id(user_id, message_id):
    daily_report = get_daily_report_student(user_id)
    daily_report.message_id = message_id
    print(daily_report.message_id)
    daily_report.save()

def exist_message_id(user_id):
    daily_report = get_daily_report_student(user_id)
    if daily_report.message_id is None:
        return False
    return True

def get_messsage_id(user_id):
    daily_report = get_daily_report_student(user_id)
    return daily_report.message_id