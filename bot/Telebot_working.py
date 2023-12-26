import random
import telebot

bot = telebot.TeleBot("6793488751:AAEgDKORpWpW5rifZ7-3PHTrqb9q237Hd3c")

@bot.message_handler(commands=['start'])
def start_game(message):
    # Отправляем сообщение с инструкцией
    bot.send_message(message.chat.id, "Отправьте список участников игры, каждого с новой строки.")

@bot.message_handler(func=lambda message: True)
def play_secret_santa(message):
    participants = message.text.split("\n")
    # Удаляем пустые строки из списка участников
    participants = list(filter(lambda x: x.strip() != "", participants))

    if len(participants) < 3:
        bot.send_message(message.chat.id, "Недостаточно участников для игры.")
    else:
        # Создаем копию списка участников
        santas = participants.copy()
        # Перемешиваем список
        random.shuffle(santas)

        # Проходим по списку участников и назначаем каждому Тайного Санту
        for i in range(len(participants)):
            giver = participants[i]
            receiver = santas[(i + 1) % len(participants)]
            m = f"{giver} дарит подарок {receiver}"
            bot.send_message(message.chat.id, m)

bot.polling()