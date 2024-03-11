from django.core.management.base import BaseCommand
from Koots.Chehovs_bot import start_bot  # Импортируем функцию start_bot из вашего файла Chehovs_bot.py

class Command(BaseCommand):
    help = 'Запускает бота Telegram'

    def handle(self, *args, **options):
        start_bot()  # Запускаем вашего бота