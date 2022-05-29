import telebot
from telebot import types
from .models import Student, DailyReport
from .buttons import *
from .logical import *

bot = telebot.TeleBot("5338255328:AAGFtVRKrFXGjxkoZWh2_-CnEBihqAQ375I", parse_mode=None)

@bot.message_handler(commands=['help', 'start'])
def start_handler(message):
    print(message)
    welcome_msg = bot.send_message(message.chat.id, "به گزارش یار خوش آمدید")
    user_id = message.chat.id
    student = Student(user_id=user_id)
    try:
        student.save()
    except:
        pass
    show_main_menu(message)

def show_main_menu(message):
    choose_msg = bot.send_message(message.chat.id, "انتخاب کن", reply_markup=gen_main())

@bot.message_handler(func = lambda message : message.text == 'بازگشت')
def register_report(message):
    show_main_menu(message)

@bot.message_handler(func = lambda message : message.text == 'پروفایل من')
def edit_profile(message):
    user_id = message.chat.id
    student_profile_text = get_student_profile_text(user_id)
    bot.send_message(message.chat.id, student_profile_text)
    bot.send_message(message.chat.id, "برای تغییر یا ثبت مشخصاتت انتخاب کن", reply_markup=gen_edit_profile())

@bot.message_handler(func = lambda message : message.text == 'گزارش یار')
def register_report(message):
    user_id = message.chat.id
    print("gozareshyar")
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if exist_report_today(user_id):
        bot.send_message(message.chat.id, "انتخاب کن", reply_markup=gen_register_report())
    else:
        bot.send_message(message.chat.id, "انتخاب کن", reply_markup=gen_show_report())


@bot.message_handler(func = lambda message : message.text == 'ثبت گزارش امروز')
def register_wake_up(message):
    user_id = message.chat.id
    create_daily_report(user_id)
    bot.send_message(message.chat.id, "برای ثبت ساعت بیدار شدنت انتخاب کن", reply_markup=gen_wake_up())


@bot.message_handler(func = lambda message : message.text == 'مشاهده و ویرایش گزارش امروز')
def add_study_subject(message):
    user_id = message.chat.id
    bot.send_message(message.chat.id, "درسی که میخوای رو انتخاب کن", reply_markup=gen_subjects())
    


@bot.callback_query_handler(lambda call: call.data.startswith("cb_"))
def set_profile_data(call):
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

@bot.callback_query_handler(lambda call: call.data.startswith("gcb_"))
def set_study_report_data(call):
    user_id = call.message.chat.id
    if call.data ==  "gcb_wake_up":
            bot.edit_message_reply_markup(message_id = call.message.message_id,
                chat_id = call.message.chat.id,
                reply_markup=gen_types_time()
                )
    elif call.data.startswith("gcb_w_"):
        if call.data == "gcb_w_4_5":
            set_wake_up_time(user_id, "4_5")
        elif call.data == "gcb_w_5_6":
            set_wake_up_time(user_id, "5_6")
        elif call.data == "gcb_w_6_7":
            set_wake_up_time(user_id, "6_7")
        elif call.data == "gcb_w_7_8":
            set_wake_up_time(user_id, "7_8")
        elif call.data == "gcb_w_8_9":
            set_wake_up_time(user_id, "8_9")
        elif call.data == "gcb_w_9_10":
            set_wake_up_time(user_id, "9_10")
        elif call.data == "gcb_w_10_11":
            set_wake_up_time(user_id, "10_11")
        elif call.data == "gcb_w_11_12":
            set_wake_up_time(user_id, "11_12")
        bot.edit_message_text(text='درسی که میخوای رو انتخاب کن', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_subjects())

    elif call.data.startswith("gcb_s_"):
        if call.data == "gcb_s_dini":
            set_subject(user_id, "دین و زندگی")
        elif call.data == "gcb_s_arabi":
            set_subject(user_id, "عربی")
        elif call.data == "gcb_s_farsi":
            set_subject(user_id, "ادبیات")
        elif call.data == "gcb_s_riazi":
            set_subject(user_id, "ریاضی")
        elif call.data == "gcb_s_zist":
            set_subject(user_id, "زیست")
        elif call.data == "gcb_s_zaban":
            set_subject(user_id, "زبان انگلیسی")
        elif call.data == "gcb_s_shimi":
            set_subject(user_id, "شیمی")
        elif call.data == "gcb_s_fizik":
            set_subject(user_id, "فیزیک")
        elif call.data == "gcb_s_zamin":
            set_subject(user_id, "زمین شناسی")
        elif call.data == "gcb_s_falsafe":
            set_subject(user_id, "فلسفه و منطق")
        elif call.data == "gcb_s_back":
            show_main_menu(call.message)
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        bot.edit_message_text(text='دقیقه ای که میخوای رو انتخاب کن', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_minutes())
        
    elif call.data.startswith("gcb_h_"):
        if call.data == "gcb_h_10":
            set_time(user_id, "10 دقیقه")
        elif call.data == "gcb_h_20":
            set_time(user_id, "20 دقیقه")
        elif call.data == "gcb_h_30":
            set_time(user_id, "30 دقیقه")
        elif call.data == "gcb_h_40":
            set_time(user_id, "40 دقیقه")
        elif call.data == "gcb_h_50":
            set_time(user_id, "50 دقیقه")
        elif call.data == "gcb_h_60":
            set_time(user_id, "60 دقیقه")
        elif call.data == "gcb_h_70":
            set_time(user_id, "70 دقیقه")
        elif call.data == "gcb_h_80":
            set_time(user_id, "80 دقیقه")
        elif call.data == "gcb_h_90":
            set_time(user_id, "90 دقیقه")
        elif call.data == "gcb_h_100":
            set_time(user_id, "100 دقیقه")
        elif call.data == "gcb_h_110":
            set_time(user_id, "110 دقیقه")
        elif call.data == "gcb_h_120":
            set_time(user_id, "120 دقیقه")
        bot.edit_message_text(text='هذف شما : ', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_study_goal())


    elif call.data.startswith("gcb_sg_"):
        if call.data == "gcb_sg_ok":
            bot.edit_message_text(text=' هدفت ثبت شد', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_start_study())
        elif call.data == "gcb_sg_cancel":
            delete_study_task(user_id)
            show_main_menu(call.message)

    elif call.data.startswith("gcb_t_"):
        if call.data == "gcb_t_start":
            bot.edit_message_text(text='مطالعت در حال انجامه ...', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_end_study())
        elif call.data == "gcb_t_cancel":
            delete_study_task(user_id)
            bot.edit_message_text(text='درسی که میخوای رو انتخاب کن', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_subjects())

        elif call.data == "gcb_sg_cancel":
            bot.edit_message_text(text='درسی که میخوای رو انتخاب کن', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_subjects())
        elif call.data == "gcb_t_end":
            bot.edit_message_text(text='\n تست هم زدی؟ مطالعه ات تموم شد', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_exist_test())
    elif call.data.startswith("gcb_test_"):
        if call.data == "gcb_test_exist":
            get_test_number_msg = bot.send_message(call.message.chat.id, 'تعداد تست هایی که زدی رو بفرست')
            bot.register_next_step_handler(get_test_number_msg, get_test_number)
            
        elif call.data == "gcb_test_without": 
               bot.edit_message_text(text='کیفیت مطالعه ات چطور بود؟', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_quality_of_study())

    elif call.data.startswith("gcb_q_"):
        if call.data == "gcb_q_1":
            set_quality_study(user_id, 1)
        elif call.data == "gcb_q_2":
            set_quality_study(user_id, 2)
        elif call.data == "gcb_q_3":
            set_quality_study(user_id, 3)
        elif call.data == "gcb_q_4":
            set_quality_study(user_id, 4)
        elif call.data == "gcb_q_5":
            set_quality_study(user_id, 5)
        bot.edit_message_text(text='کیفیت مطالعه ات ثبت شد', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_sleep())

    elif call.data.startswith("gcb_sl"):
        if call.data == "gcb_sleep_time":
            bot.edit_message_text(text='برای ثبت ساعت خوابیدنت انتخاب کن', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_types_time_sleep())
        elif call.data == "gcb_sleep_back": 
            bot.edit_message_text(text='درسی که میخوای رو انتخاب کن', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=gen_subjects())
                              
    elif call.data.startswith("gcb_ts_"):
        if call.data == "gcb_ts_20_21":
            set_sleep_time(user_id, "20_21")
        elif call.data == "gcb_ts_21_22":
            set_sleep_time(user_id, "21_22")
        elif call.data == "gcb_ts_22_23":
            set_sleep_time(user_id, "22_23")
        elif call.data == "gcb_ts_23_24":
            set_sleep_time(user_id, "23_24")
        elif call.data == "gcb_ts_24_1":
            set_sleep_time(user_id, "24_1")
        elif call.data == "gcb_ts_1_2":
            set_sleep_time(user_id, "1_2")
        elif call.data == "gcb_ts_2_3":
            set_sleep_time(user_id, "2_3")
        elif call.data == "gcb_ts_3_4":
            set_sleep_time(user_id, "3_4")
            bot.edit_message_text(text= 'ساعت خوابت ثبت شد', 
                              message_id=call.message.id, 
                              chat_id=call.message.chat.id,
                              reply_markup=None)
            show_main_menu(call.message)
            
    else:
        show_main_menu(call.message)





@bot.message_handler(content_types=['text'])
def get_first_name(message):
    if message.text == 'انصراف':
        show_main_menu(message)
    else:
        try:
            user_fname = message.text
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
                user_id = message.chat.id
                student = Student.objects.filter(user_id=user_id).update(grade=user_grade)
                bot.send_message(message.chat.id, "پایه تحصیلیت ثبت شد", reply_markup=gen_main())
            else:
                bot.send_message(message.chat.id, "پایه تحصیلیت ثبت نشد")
        except Exception as e:
            bot.send_message(message.chat.id, "Exception")


@bot.message_handler(content_types=['text'])
def get_test_number(message):
    try:
        user_id = message.chat.id
        print(user_id)
        set_test_number(user_id, message.text)
        print(message.text)
        bot.send_message(message.chat.id, " تعداد تست هات ثبت شد \n کیفیت مطالعه ات چطور بود؟",  reply_markup=gen_quality_of_study())
    except:
        pass


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

    
