from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import telebot
from telebot import types

def gen_grade():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True,  resize_keyboard=True)
    dahom_btn = types.KeyboardButton('دهم')
    yazdahom_btn = types.KeyboardButton('یازدهم')
    davazdahom_btn = types.KeyboardButton('دوازدهم')
    markup.add(dahom_btn, yazdahom_btn, davazdahom_btn)
    return markup

def gen_main():
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True,  resize_keyboard=True)
    profile_btn = types.KeyboardButton('پروفایل من')
    gozareshyar_btn = types.KeyboardButton('گزارش یار')
    markup.add(profile_btn, gozareshyar_btn)
    return markup

def remove_markup(markup):
    markup = types.ReplyKeyboardRemove(selective=False)
    return markup

def gen_register_report():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True)
    register_btn = types.KeyboardButton('ثبت گزارش امروز')
    back_btn = types.KeyboardButton('بازگشت')
    markup.add(register_btn, back_btn)
    return markup

def gen_wake_up():
    markup = InlineKeyboardMarkup(row_width=1)
    wake_up_btn = InlineKeyboardButton("ثبت ساعت بیدار شدنت", callback_data="gcb_wake_up")
    markup.add(wake_up_btn)
    return markup

def gen_types_time():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row_width = 2
    wake_up_btn1 = InlineKeyboardButton("4_5", callback_data="gcb_w_4_5")
    wake_up_btn2 = InlineKeyboardButton("5_6", callback_data="gcb_w_5_6")
    wake_up_btn3 = InlineKeyboardButton("6_7", callback_data="gcb_w_6_7")
    wake_up_btn4 = InlineKeyboardButton("7_8", callback_data="gcb_w_7_8")
    wake_up_btn5 = InlineKeyboardButton("8_9", callback_data="gcb_w_8_9")
    wake_up_btn6 = InlineKeyboardButton("9_10", callback_data="gcb_w_9_10")
    wake_up_btn7 = InlineKeyboardButton("10_11", callback_data="gcb_w_10_11")
    wake_up_btn8 = InlineKeyboardButton("11_12", callback_data="gcb_w_11_12")
    markup.add(wake_up_btn1, wake_up_btn2, wake_up_btn3, wake_up_btn4,
               wake_up_btn5, wake_up_btn6, wake_up_btn7, wake_up_btn8)
    return markup

def gen_edit_profile():
    markup = InlineKeyboardMarkup(row_width=1)
    fname_btn = InlineKeyboardButton("نام", callback_data="cb_fname")
    lname_btn = InlineKeyboardButton("نام خانوادگی", callback_data="cb_lname")
    phone_number_btn = InlineKeyboardButton("تلفن همراه", callback_data="cb_phone_number")
    grade_btn = InlineKeyboardButton("پایه تحصیلی", callback_data="cb_grade")
    markup.add(fname_btn, lname_btn, phone_number_btn, grade_btn)
    return markup

def gen_cancel():
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True,  resize_keyboard=True)
    cancel_btn = types.KeyboardButton('انصراف')
    markup.add(cancel_btn)
    return markup

def gen_share_phone():
    markup = types.ReplyKeyboardMarkup (row_width=1, resize_keyboard=True) 
    share_phone_btn = types.KeyboardButton ('فرستادن شمارت', request_contact = True)
    cancel_btn =  types.KeyboardButton('انصراف')
    markup.add (share_phone_btn, cancel_btn)
    return markup

def gen_subjects():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row_width = 2
    dinozendgi_btn = InlineKeyboardButton("دین و زندگی", callback_data="gcb_s_dini")
    arabi_btn = InlineKeyboardButton("عربی", callback_data="gcb_s_arabi")
    farsi_btn = InlineKeyboardButton("ادبیات", callback_data="gcb_s_farsi")
    riazi_btn = InlineKeyboardButton("ریاضی", callback_data="gcb_s_riazi")
    zist_btn = InlineKeyboardButton("زیست", callback_data="gcb_s_zist")
    zaban_btn = InlineKeyboardButton("زبان انگلیسی", callback_data="gcb_s_zaban")
    shimi_btn = InlineKeyboardButton("شیمی", callback_data="gcb_s_shimi")
    fizik_btn = InlineKeyboardButton("فیزیک", callback_data="gcb_s_fizik")
    zamin_btn = InlineKeyboardButton("زمین شناسی", callback_data="gcb_s_zamin")
    falsafe_btn = InlineKeyboardButton("فلسفه و منطق", callback_data="gcb_s_falsafe")
    back_btn = InlineKeyboardButton("بازگشت", callback_data="gcb_s_back",row_width=1)
    markup.add(dinozendgi_btn, arabi_btn, farsi_btn, riazi_btn, zist_btn, zaban_btn, 
               shimi_btn,fizik_btn, zamin_btn, falsafe_btn, back_btn)
    return markup

def gen_minutes():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row_width = 2
    min_10_btn = InlineKeyboardButton("10", callback_data="gcb_h_10")
    min_20_btn = InlineKeyboardButton("20", callback_data="gcb_w_20")
    min_30_btn = InlineKeyboardButton("30", callback_data="gcb_w_30")
    min_40_btn = InlineKeyboardButton("40", callback_data="gcb_w_40")
    min_50_btn = InlineKeyboardButton("50", callback_data="gcb_w_50")
    min_60_btn = InlineKeyboardButton("60", callback_data="gcb_w_60")
    min_70_btn = InlineKeyboardButton("70", callback_data="gcb_w_70")
    min_80_btn = InlineKeyboardButton("80", callback_data="gcb_w_80")
    min_90_btn = InlineKeyboardButton("90", callback_data="gcb_w_90")
    min_100_btn = InlineKeyboardButton("100", callback_data="gcb_w_100")
    min_110_btn = InlineKeyboardButton("110", callback_data="gcb_w_110")
    min_120_btn = InlineKeyboardButton("120", callback_data="gcb_w_120")
    markup.add(min_10_btn, min_20_btn, min_30_btn, min_40_btn, min_50_btn,
               min_60_btn, min_70_btn, min_80_btn, min_90_btn, min_100_btn,
               min_110_btn, min_120_btn)
    return markup




