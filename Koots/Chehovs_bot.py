import telebot
from telebot import types
from Koots.models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

# Список ID пользователей, которым бот будет отправлять сообщения
user_ids = []

@receiver(post_save, sender=Order)
def send_new_order(sender, instance, **kwargs):
    buyer = instance.buyer
    sheet = instance.sheet
    message = f"Новый заказ: {instance.id}\nЗаказчик: {buyer.name} {buyer.surname}\nАдрес: {instance.address}\nДоставка: {instance.delivery}\nТелефон: {instance.phone}\nTelegram: {instance.telegram}\nНотная книга: {sheet.name}, Жанр: {sheet.genre}, Композиторы: {sheet.compositors}, Цена: {sheet.price}\nДополнительно: {instance.additional}"
    # Отправляем сообщение всем пользователям в списке
    for user_id in user_ids:
        # Отправляем только первое изображение нотной книги с текстом как подписью
        if sheet.images.exists():
            bot.send_photo(user_id, sheet.images.first().image, caption=message)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я ваш бот.')
    # Создаем клавиатуру с кнопкой
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_show_orders = types.KeyboardButton(text="Показать заказы")
    keyboard.add(button_show_orders)
    bot.send_message(message.chat.id, "Выберите команду:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Показать заказы")
def show_orders(message):
    orders = Order.objects.all()
    for order in orders:
        buyer = order.buyer
        sheet = order.sheet
        message_text = f"Заказ: {order.id}\nЗаказчик: {buyer.name} {buyer.surname}\nАдрес: {order.address}\nДоставка: {order.delivery}\nТелефон: {order.phone}\nTelegram: {order.telegram}\nДополнительно: {order.additional}\nНотная книга: {sheet.name}, Жанр: {sheet.genre}, Композиторы: {sheet.compositors}, Цена: {sheet.price}"
        for user_id in user_ids:
            # Отправляем только первое изображение нотной книги с текстом как подписью
            if sheet.images.exists():
                bot.send_photo(user_id, sheet.images.first().image, caption=message_text)

def start_bot():
    bot.polling(none_stop=True)
