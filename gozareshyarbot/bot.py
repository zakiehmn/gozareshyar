import telebot
from telebot import types
from .models import Student
from .buttons import *
from .logical import *

bot = telebot.TeleBot("5338255328:AAGFtVRKrFXGjxkoZWh2_-CnEBihqAQ375I", parse_mode=None)

user_dict = {}


@bot.message_handler(commands=['help', 'start'])
def start_handler(message):
    welcome_msg = bot.send_message(message.chat.id, "به گزارش یار خوش آمدید")
    user_id = message.chat.id
    user_dict['id'] = user_id
    print(user_id)
    student = Student(user_id=user_id)
    student.save()
    show_main_menu(message)

def show_main_menu(message):
    choose_msg = bot.send_message(message.chat.id, "انتخاب کن", reply_markup=gen_main())

@bot.message_handler(func = lambda message : message.text == 'پروفایل من')
def edit_profile(message):
    bot.send_message(message.chat.id, "برای تغییر یا ثبت مشخصاتت انتخاب کن", reply_markup=gen_edit_profile())

@bot.message_handler(func = lambda message : message.text == 'گزارش یار')
def register_report(message):
    bot.send_message(message.chat.id, "انتخاب کن", reply_markup=gen_register_report())

@bot.message_handler(func = lambda message : message.text == 'ثبت گزارش امروز')
def register_wake_up(message):
    bot.send_message(message.chat.id, "برای ثبت ساعت بیدار شدنت انتخاب کن", reply_markup=gen_wake_up())


@bot.callback_query_handler(lambda call: call.data.startswith("cb_"))
def register_wake_up_time(call):
    if call.data == "cb_fname":
        get_fname_msg = bot.send_message(call.message.chat.id, 'اسمت رو بنویس و ارسال کن', reply_markup=gen_cancel())
        bot.register_next_step_handler(get_fname_msg, get_first_name)
    elif call.data == "cb_lname":
        get_lname_msg = bot.send_message(call.message.chat.id, 'فامیلت رو بنویس و ارسال کن', reply_markup=gen_cancel())
        bot.register_next_step_handler(get_lname_msg, get_last_name)
    elif call.data == "cb_phone_number":
        get_phone_msg = bot.send_message(call.message.chat.id, 'شماره تلفنت رو با دکمه زیر ارسال کن', reply_markup=gen_share_phone())
        bot.register_next_step_handler(get_phone_msg, get_phone_number)
    elif call.data == "cb_grade":
        get_grade_msg = bot.send_message(call.message.chat.id,'پایه تحصیلیت رو ارسال کن', reply_markup=gen_grade())
        bot.register_next_step_handler(get_grade_msg, get_grade)

@bot.message_handler(content_types=['text'])
def get_first_name(message):
    if message.text == 'انصراف':
        show_main_menu(message)
    else:
        try:
            user_fname = message.text
            user_dict['first_name'] = user_fname
            user_id = message.chat.id
            student = Student.objects.filter(user_id=user_id).update(first_name=user_fname)
            bot.send_message(message.chat.id, "اسمت ثبت شد", reply_markup=gen_main())
        except Exception as e:
            bot.send_message(message.chat.id, "Exception")

@bot.message_handler(content_types=['text'])
def get_last_name(message):
    if message.text == 'انصراف':
        show_main_menu(message)
    else:
        try:
            user_lname = message.text
            user_dict['last_name'] = user_lname
            user_id = message.chat.id
            student = Student.objects.filter(user_id=user_id).update(last_name=user_lname)
            bot.send_message(message.chat.id, "فامیلت ثبت شد",  reply_markup=gen_main())
        except Exception as e:
            bot.send_message(message.chat.id, "Exception")

@bot.message_handler(content_types=['contact', 'text'])
def get_phone_number(message):
    if message.text == 'انصراف':
        show_main_menu(message)
    else:
        try:
            phone_number = message.contact.phone_number
            user_dict['phone_number'] = phone_number
            user_id = message.chat.id
            student = Student.objects.filter(user_id=user_id).update(phone_number=phone_number)
            bot.send_message(message.chat.id, "شمارت ثبت شد",  reply_markup=gen_main())
        except Exception as e:
            bot.send_message(message.chat.id, "Exception")

@bot.message_handler(content_types=['text'])
def get_grade(message):
    if message.text == 'انصراف':
        show_main_menu(message)
    else:
        try:
            if message.text == "دهم" or "یازدهم" or "دوازدهم" :
                user_grade = message.text
                user_dict['grade'] = message.text
                print(message.text)
                # markup_remove = remove_markup(gen_grade)
                user_id = message.chat.id
                student = Student.objects.filter(user_id=user_id).update(grade=user_grade)
                bot.send_message(message.chat.id, "پایه تحصیلیت ثبت شد", reply_markup=gen_main())
            else:
                bot.send_message(message.chat.id, "پایه تحصیلیت ثبت نشد")
        except Exception as e:
            bot.send_message(message.chat.id, "Exception")




@bot.message_handler(func = lambda message : message.text == 'گزارش یار')
def register_report(message):
    bot.send_message(message.chat.id, "انتخاب کن", reply_markup=gen_register_report())

@bot.message_handler(func = lambda message : message.text == 'ثبت گزارش امروز')
def register_wake_up(message):
    bot.send_message(message.chat.id, "برای ثبت ساعت بیدار شدنت انتخاب کن", reply_markup=gen_wake_up())

@bot.callback_query_handler(func=lambda call: True)
def register_wake_up_time(call):
        print(call.data)
        if call.data == "cb_wake_up":
            bot.edit_message_reply_markup(
                message_id = call.message.message_id,
                chat_id = call.message.chat.id,
                reply_markup=gen_types_time()
                )
            print("ok")
        else:
            print("no")
    

@bot.callback_query_handler(func=lambda call: True)
def register_wake_up_time(call):
        print(call.data)
        if call.data == "cb_wake_up":
            bot.edit_message_reply_markup(
                message_id = call.message.message_id,
                chat_id = call.message.chat.id,
                reply_markup=gen_types_time()
                )
            print("ok")
        else:
            print("no")
    

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

    
