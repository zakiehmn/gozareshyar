from .models import Student

def get_student(user_id):
    student = Student.objects.filter(user_id=user_id).last()
    return student

def get_student_profile_text(user_id):
    student = get_student(user_id)
    fist_name = student.first_name
    last_name = student.last_name
    phone_number = student.phone_number
    grade = student.grade
    student_profile_text = "اطلاعاتت:\n نام:{} \n نام خانوادگی:{} \n شماره تلفن:{} \n پایه تحصیلی:{} \n ".format(fist_name, last_name, phone_number, grade)
    return student_profile_text