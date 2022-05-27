from django.core.management.base import BaseCommand
from gozareshyarbot.bot import *
import telebot


class Command(BaseCommand):
    help = 'run bot.py'

    def handle(self, *args, **kwargs):
        
        # bot = telebot.TeleBot("5338255328:AAGFtVRKrFXGjxkoZWh2_-CnEBihqAQ375I", parse_mode=None)
        
        bot.infinity_polling()