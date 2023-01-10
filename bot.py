import telebot
import random
bot = telebot.TeleBot('5829941809:AAGwjGOmycbsNlMaVYXdLddtQ6w-8FuiBzc');
@bot.message_handler(content_types=['photo', 'text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.chat.id, '''Вот общий список команд:
        /help - посмотреть все команды
        /all [text] - тегнуть всех (admin only)
        /chatinfo - инфо о чате
        /link - получить ссылку на беседу
        /ds - получить ссылку на дс
        /off - выключить бота (admin only)''')
        print(f'/help command successfully done in "{message.chat.title}" ID:{message.chat.id} SENDER:{message.from_user.username}')
    if message.text[:4] == '/all':
        if message.from_user.id == 687900545:
            bot.send_message(message.chat.id, f'@solukky @Sovaaaaa @MahachKala08 @rhuller @Triggered_dude @CherkasovNikita @tuberculum_caroticum @tytnik @Kowmapuk666 @EgorVysotsckij @MekoFLX @dub_nik217 @Dark_shadow_blunts @Anelibri \n\n {message.text[5:]}')
            print(f'/all command successfully done in "{message.chat.title}" ID:{message.chat.id} SENDER:{message.from_user.username}')
        if message.from_user.id != 687900545:
            bot.send_message(message.chat.id, 'Вы не являетесь администратором данной группы, поэтому не можете использовать эту команду')
            print(f'/all command not done (user is not an administrator) in "{message.chat.title}" ID:{message.chat.id} SENDER:{message.from_user.username}')
    if message.text == '/link':
        bot.send_message(message.chat.id, f'⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ \nhttps://t.me/+sqIXjp-OQHJiMDIy \n⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧')
        print(f'/link command successfully done in "{message.chat.title}" ID:{message.chat.id} SENDER:{message.from_user.username}')
    if message.text == '/ds':
        bot.send_message(message.chat.id, f'⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ ⇩ \nhttps://discord.gg/P9PkSbM8Xz \n⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧ ⇧')
        print(f'/ds command successfully done in "{message.chat.title}" ID:{message.chat.id} SENDER:{message.from_user.username}')
    if message.text == '/chatinfo':
        bot.send_message(message.chat.id, f'Chat ID: {message.chat.id}\nChat Name: {message.chat.title}\nChat Type: {message.chat.type}')
        print(f'/chatinfo command successfully done in "{message.chat.title}" ID:{message.chat.id} SENDER:{message.from_user.username}')
    if message.text == '/off':
        if message.from_user.id == 687900545:
            bot.send_message(message.chat.id, 'Завершаю работу, хорошего дня!')
            print(f'Bot stopped work because of /off command in "{message.chat.title}" ID:{message.chat.id} SENDER:{message.from_user.username}')
            bot.send_message(message.fndjfjjdsfkjdsfljdsjfk)
        if message.from_user.id != 687900545:
            bot.send_message(message.chat.id, 'Вы не являетесь администратором, поэтому не можете завершить работу бота.')
            print(f'/off command not done (user is not an administrator) in "{message.chat.title}" ID:{message.chat.id} SENDER:{message.from_user.username}')
    if message.text[:3] == '/to':
        if message.from_user.id == 687900545:
            bot.send_message(829033617, f'{message.text[4:]}\nFrom Vlad')
            print(f'/tok command successfully done to Ksusha')
        if message.from_user.id == 829033617:
            bot.send_message(687900545, f'{message.text[4:]}\nFrom Ksusha')
            print(f'/tov command successfully done to Vlad')
    if message.from_user.id == 829033617:
        message.text = message.text.lower()
        if message.text == '/st':
            print('Ksusha used /st to learn commands')
            bot.send_message(message.from_user.id, '''/st - узнать личные команды (только для тебя)
Грустно - ответ на грусть❤
Мне грустно - ответ на грусть❤
Грущу - ответ на грусть❤
            
Скучаю - ответ на тоску❤
Я скучаю - ответ на тоску❤
Скучаю по тебе - ответ на тоску❤
            
Люблю - ответ на любовь❤
Я тебя люблю - ответ на любовь❤
Люблю тебя - ответ на любовь❤

Вопрос ("?" в конце сообщения) - получить случайный ответ на твой вопрос❤
            
Вместо команды /tov, которая использовалась для отправки сообщения мне, теперь используй просто /to
Пример: /to Я тебя люблю❤''')
        if message.text == 'мне грустно' or message.text == 'грустно' or message.text == 'грущу':
            a = round(random.random()*10)
            print('Ksusha said that she is sad')
            if a == 1:
                bot.send_message(message.from_user.id, 'Солнышко, не грусти, помни что я тебя люблю❤')
            if a == 2:
                bot.send_message(message.from_user.id, 'Давай когда я приду, ты расскажешь мне, почему грустишь?❤')
            if a == 3:
                bot.send_message(message.from_user.id, 'Расскажи мне в лс, почему ты грустишь?❤')
            if a == 4:
                bot.send_message(message.from_user.id, 'Я тебя люблю, не грусти, зайка❤❤❤')
            if a == 5:
                bot.send_message(message.from_user.id, 'Если тебя кто то обидел - расскажи мне в лс❤')
            if a == 6:
                bot.send_message(message.from_user.id, 'Напиши мне в лс, а я прочитаю при первой же возможности❤❤❤')
            if a == 7:
                bot.send_message(message.from_user.id, 'Когда я буду в сети, мы обязательно об этом поговорим❤')
            if a == 8:
                bot.send_message(message.from_user.id, 'Не грусти, мой жопик ❤')
            if a == 9:
                bot.send_message(message.from_user.id, 'Попробуй занять себя чем-нибудь, вдруг грусть уйдет')
            if a == 10:
                bot.send_message(message.from_user.id, 'Я тебя люблю, поэтому не грусти ❤')
        if message.text == 'я скучаю' or message.text == 'скучаю по тебе' or message.text == 'скучаю':
            print('Ksusha said that she miss me')
            a = round(random.random()*5)
            if a == 1:
                bot.send_message(message.from_user.id, 'Я тоже скучаю, малыш❤')
            if a == 2:
                bot.send_message(message.from_user.id, 'Солнце, посмотри совместные фотки❤')
            if a == 3:
                bot.send_message(message.from_user.id, 'Зайчик, отвлекись от этого, например поиграй❤')
            if a == 4:
                bot.send_message(message.from_user.id, 'Зайка, я очень сильно тебя люблю❤')
            if a == 5:
                bot.send_message(message.from_user.id, 'Когда я буду в сети - мы обязательно пообщаемся❤')
        if message.text == 'люблю' or message.text == 'люблю тебя' or message.text == 'я тебя люблю':
            print('Ksusha said that she loves you')
            a = round(random.random() * 10)
            if a == 1:
                bot.send_message(message.from_user.id, 'И я тебя люблю❤❤❤')
            if a == 2:
                bot.send_message(message.from_user.id, 'Я сильнее❤')
            if a == 3:
                bot.send_message(message.from_user.id, 'А я тебя обожаю❤')
            if a == 4:
                bot.send_message(message.from_user.id, 'Ты мой малыш❤❤❤')
            if a == 5:
                bot.send_message(message.from_user.id, 'Ты у меня самая лучшая❤')
            if a == 6:
                bot.send_message(message.from_user.id, 'А я все равно сильнее люблю❤❤❤')
            if a == 7:
                bot.send_message(message.from_user.id, 'Целую❤❤❤')
            if a == 8:
                bot.send_message(message.from_user.id, 'Представь что я тебя обнял❤')
            if a == 9:
                bot.send_message(message.from_user.id, 'Люблю люблю люблю❤❤❤')
            if a == 10:
                bot.send_message(message.from_user.id, 'Мое солнышко❤')
        if message.text[-1:] == '?':
            a = round(random.random()*5)
            print('Ksusha asked a question')
            if a == 1:
                bot.send_message(message.from_user.id, 'Точно Да')
            if a == 2:
                bot.send_message(message.from_user.id, 'Скорее всего Да')
            if a == 3:
                bot.send_message(message.from_user.id, 'Не знаю')
            if a == 4:
                bot.send_message(message.from_user.id, 'Скорее всего Нет')
            if a == 5:
                bot.send_message(message.from_user.id, 'Точно Нет')
bot.polling(none_stop=True, interval=0)