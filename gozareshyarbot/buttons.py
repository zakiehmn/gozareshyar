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
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    register_btn = types.KeyboardButton('ثبت گزارش امروز')
    back_btn = types.KeyboardButton('بازگشت')
    markup.add(register_btn, back_btn)
    return markup

def gen_wake_up():
    markup = InlineKeyboardMarkup(row_width=1)
    wake_up_btn = InlineKeyboardButton("ثبت ساعت بیدار شدنت", callback_data="cb_wake_up")
    markup.add(wake_up_btn)
    return markup

def gen_types_time():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row_width = 2
    wake_up_btn = InlineKeyboardButton("8_9", callback_data="cb_8_9")
    markup.add(wake_up_btn)
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
    markup = types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True) 
    share_phone_btn = types.KeyboardButton ('فرستادن شمارت', request_contact = True)
    cancel_btn =  types.KeyboardButton('انصراف')
    markup.add (share_phone_btn, cancel_btn)
    return markup