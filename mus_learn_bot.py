from telebot import *
import webbrowser
import random
import PIL
from PIL import Image
import time
from config import Token


bot = telebot.TeleBot(Token)

do = Image.open("do.jpg").resize((100, 100))
re = Image.open("re.jpg").resize((100, 100))
mi = Image.open("mi.jpg").resize((100, 100))
fa = Image.open("fa.jpg").resize((100, 100))
sol = Image.open("sol.jpg").resize((100, 100))
la = Image.open("la.jpg").resize((100, 100))
si = Image.open("si.jpg").resize((100, 100))

list_img = [do, re, mi, fa, sol, la, si]

#выбор ноты
comp_nota = random.choice(list_img)

area = (0,0,70,100)

def chose_nots(n):
    nota = n.resize((100, 100))
    return nota


#обрезание название
def cats_nots(n):
    area = (0,0,70,100)
    cut_nota = n.resize((100, 100)).crop(area)
    return cut_nota


# список с обрезанными нотами
list_cut_nots = []
for i in list_img:
    с = cats_nots(i)
    list_cut_nots.append(с)




list_nots = ["ДО", "РЕ", "МИ", "ФА", "СОЛЬ", "ЛЯ", "СИ"]

# словарь с названиями и нотами
nota_dict = dict(zip(list_nots, list_img))
cut_dict = dict(zip(list_nots, list_cut_nots))

cut_choise= []
def full_card(cut_ch):
    cut_number = list_cut_nots.index(cut_ch)
    full_card_notes = list_img[cut_number]
    return full_card_notes

#показывает обрезанную ноту, по индексу
def music(w):
        count = -1
        for i in list_nots:
            count += 1
            if i in w:
                index_nota = list_img[count]

                return chose_nots(index_nota)

list_words = ["ДOМ", "РЕДИС", "МИНОР", "ФАКТ", "СОЛЬ", "ПЛЯЖ", "СИТО"]
list_rebus = ["**M", "**ДИС", "**НОР", "**КТ", "****", "П**Ж", "**ТО"]

#определение полного слова по ребусу
rebus_list = []
def full_word(w):
    rebus_number = list_rebus.index(w)
    full_w = list_words[rebus_number]

    return full_w

correct_n = []
def correct_nota(w):
    rebus_n = list_rebus.index(w)
    corr_n = list_img[rebus_n]
    return corr_n

# открывает клавиатуру
muz_text = open("img.png", "rb")
muz_text1 = open("img.png", "rb")
url = "http://pianizator.ru/piano-tutorial/622-mortal-kombat-mortal-kombat-kak-igrat-na-pianino.html"

# открывает mp3

music_file = open('Mortal Kombat - Maine Theme (Original).mp3','rb')
midi_file = open('combat.mp3','rb')

# открывает карточки_подсказки
help_1_oktava = open("Page1.jpg","rb")
help_2_oktava = open("Page2.jpg","rb")


# кнопки старта
@bot.message_handler(commands=['start'])
def start(message):
    button = types.InlineKeyboardMarkup()
    button_game1 = types.InlineKeyboardButton(text="Знакомство", callback_data="game1")
    button_game2 = types.InlineKeyboardButton(text="Ребус", callback_data="game2")
    button_game3 = types.InlineKeyboardButton(text="Угадай ноту", callback_data="game3")
    button_game4 = types.InlineKeyboardButton(text="Финал", callback_data="game4")
    button.add(button_game1,button_game2, button_game3, button_game4)
    bot.send_message(message.chat.id,"Привет.Давай учить ноты!! Выбери игру", reply_markup=button)


# игра 1 знакомство с нотами
@bot.callback_query_handler(func = lambda call: True)
def call_back_inline(call):
    if call.data == "game1":
        bot.send_message(call.message.chat.id, "Выбери название ноты. Я покажу её запись")

        button_game1 = types.InlineKeyboardMarkup()
        button_do= types.InlineKeyboardButton(text="ДО", callback_data="DO")
        button_re = types.InlineKeyboardButton(text="РЕ", callback_data="RE")
        button_mi = types.InlineKeyboardButton(text="МИ", callback_data="MI")
        button_fa = types.InlineKeyboardButton(text="ФА", callback_data="FA")
        button_sol = types.InlineKeyboardButton(text="СОЛЬ", callback_data="SOL")
        button_la = types.InlineKeyboardButton(text="ЛЯ", callback_data="LA")
        button_si= types.InlineKeyboardButton(text="СИ", callback_data="SI")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")

        button_game1.add(button_do, button_re, button_mi, button_fa, button_sol, button_la, button_si, button_end)
        bot.send_message(call.message.chat.id, "Выбери ноту", reply_markup=button_game1)

    if call.data == "DO":
        bot.send_photo(call.message.chat.id, do)
    elif call.data == "RE":
        bot.send_photo(call.message.chat.id, re)
    elif call.data == "MI":
        bot.send_photo(call.message.chat.id, mi)
    elif call.data == "FA":
        bot.send_photo(call.message.chat.id, fa)
    elif call.data == "SOL":
        bot.send_photo(call.message.chat.id, sol)
    elif call.data == "LA":
        bot.send_photo(call.message.chat.id, la)
    elif call.data == "SI":
        bot.send_photo(call.message.chat.id, si)
    elif call.data == "End":
        button = types.InlineKeyboardMarkup()
        button_game1 = types.InlineKeyboardButton(text="Знакомство", callback_data="game1")
        button_game2 = types.InlineKeyboardButton(text="Ребус", callback_data="game2")
        button_game3 = types.InlineKeyboardButton(text="Кто это?", callback_data="game3")
        button_game4 = types.InlineKeyboardButton(text="Финал", callback_data="game4")
        button.add(button_game1, button_game2, button_game3, button_game4)
        bot.send_message(call.message.chat.id, "Привет.Давай учить ноты!! Выбери игру", reply_markup=button)



# 2игра ребус

    if call.data == "game2":

        bot.send_message(call.message.chat.id, "Найди название ноты в слове")
        # выбор ребуса компьютером
        rebus_word = random.choice(list_rebus)
        rebus_list.append(rebus_word)
        correct_n.append(rebus_word)



        bot.send_message(call.message.chat.id, rebus_word)
        time.sleep(2)

        button_game2 = types.InlineKeyboardMarkup()
        button_do = types.InlineKeyboardButton(text="ДО", callback_data="DO2")
        button_re = types.InlineKeyboardButton(text="РЕ", callback_data="RE2")
        button_mi = types.InlineKeyboardButton(text="МИ", callback_data="MI2")
        button_fa = types.InlineKeyboardButton(text="ФА", callback_data="FA2")
        button_sol = types.InlineKeyboardButton(text="СОЛЬ", callback_data="SOL2")
        button_la = types.InlineKeyboardButton(text="ЛЯ", callback_data="LA2")
        button_si = types.InlineKeyboardButton(text="СИ", callback_data="SI2")


        button_game2.add(button_do, button_re, button_mi, button_fa, button_sol, button_la, button_si)
        bot.send_message(call.message.chat.id, "Выбери ноту", reply_markup=button_game2)


    elif call.data == "DO2":
        bot.send_message(call.message.chat.id, "Сравни свой ответ с правильным")
        time.sleep(2)
        bot.send_message(call.message.chat.id, "Ты выбрал")
        bot.send_photo(call.message.chat.id, do)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, correct_nota(rebus_list[-1]))
        bot.send_message(call.message.chat.id, full_word(rebus_list[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)
        bot.send_photo(call.message.chat.id, correct_nota(rebus_list[-1]))


    elif call.data == "RE2":
        bot.send_message(call.message.chat.id, "Сравни свой ответ с правильным")
        time.sleep(2)
        bot.send_message(call.message.chat.id, "Ты выбрал")
        bot.send_photo(call.message.chat.id, re)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, correct_nota(rebus_list[-1]))
        bot.send_message(call.message.chat.id, full_word(rebus_list[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "MI2":
        bot.send_message(call.message.chat.id, "Сравни свой ответ с правильным")
        time.sleep(2)
        bot.send_message(call.message.chat.id, "Ты выбрал")
        bot.send_photo(call.message.chat.id, mi)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, correct_nota(rebus_list[-1]))
        bot.send_message(call.message.chat.id, full_word(rebus_list[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "FA2":
        bot.send_message(call.message.chat.id, "Сравни свой ответ с правильным")
        time.sleep(2)
        bot.send_message(call.message.chat.id, "Ты выбрал")
        bot.send_photo(call.message.chat.id, fa)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, correct_nota(rebus_list[-1]))
        bot.send_message(call.message.chat.id, full_word(rebus_list[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "SOL2":
        bot.send_message(call.message.chat.id, "Сравни свой ответ с правильным")
        time.sleep(2)
        bot.send_message(call.message.chat.id, "Ты выбрал")
        bot.send_photo(call.message.chat.id, sol)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, correct_nota(rebus_list[-1]))
        bot.send_message(call.message.chat.id, full_word(rebus_list[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "LA2":
        bot.send_message(call.message.chat.id, "Сравни свой ответ с правильным")
        time.sleep(2)
        bot.send_message(call.message.chat.id, "Ты выбрал")
        bot.send_photo(call.message.chat.id, la)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, correct_nota(rebus_list[-1]))
        bot.send_message(call.message.chat.id, full_word(rebus_list[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "SI2":
        bot.send_message(call.message.chat.id, "Сравни свой ответ с правильным")
        time.sleep(2)
        bot.send_message(call.message.chat.id, "Ты выбрал")
        bot.send_photo(call.message.chat.id, si)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, correct_nota(rebus_list[-1]))
        bot.send_message(call.message.chat.id, full_word(rebus_list[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "Cont":
        bot.send_message(call.message.chat.id, "Поехали!")
        bot.send_message(call.message.chat.id, "Найди название ноты в слове")
        rebus_word = random.choice(list_rebus)
        rebus_list.append(rebus_word)
        w = rebus_list[-1]

        bot.send_message(call.message.chat.id, rebus_word)
        time.sleep(2)

        button_game2 = types.InlineKeyboardMarkup()
        button_do = types.InlineKeyboardButton(text="ДО", callback_data="DO2")
        button_re = types.InlineKeyboardButton(text="РЕ", callback_data="RE2")
        button_mi = types.InlineKeyboardButton(text="МИ", callback_data="MI2")
        button_fa = types.InlineKeyboardButton(text="ФА", callback_data="FA2")
        button_sol = types.InlineKeyboardButton(text="СОЛЬ", callback_data="SOL2")
        button_la = types.InlineKeyboardButton(text="ЛЯ", callback_data="LA2")
        button_si = types.InlineKeyboardButton(text="СИ", callback_data="SI2")


        button_game2.add(button_do, button_re, button_mi, button_fa, button_sol, button_la, button_si)
        bot.send_message(call.message.chat.id, "Выбери ноту", reply_markup=button_game2)
#игра 3
    elif call.data == "game3":
        comp_nota_cut = random.choice(list_cut_nots)
        cut_choise.append(comp_nota_cut)

        bot.send_photo(call.message.chat.id, comp_nota_cut)
        bot.send_message(call.message.chat.id, "Какая это нота?")

        button_nots = types.InlineKeyboardMarkup()
        button_do3 = types.InlineKeyboardButton(text="ДО", callback_data="DO3")
        button_re3 = types.InlineKeyboardButton(text="РЕ", callback_data="RE3")
        button_mi3 = types.InlineKeyboardButton(text="МИ", callback_data="MI3")
        button_fa3 = types.InlineKeyboardButton(text="ФА", callback_data="FA3")
        button_sol3 = types.InlineKeyboardButton(text="СОЛЬ", callback_data="SOL3")
        button_la3 = types.InlineKeyboardButton(text="ЛЯ", callback_data="LA3")
        button_si3 = types.InlineKeyboardButton(text="СИ", callback_data="SI3")


        button_nots.add(button_do3, button_re3, button_mi3, button_fa3,
                         button_sol3, button_la3, button_si3)
        bot.send_message(call.message.chat.id, "Выбери ноту", reply_markup=button_nots)

    elif call.data == "Cont3":
        bot.send_message(call.message.chat.id, "Загадываем снова")
        comp_nota_cut = random.choice(list_cut_nots)
        cut_choise.append(comp_nota_cut)
        bot.send_photo(call.message.chat.id, comp_nota_cut)
        bot.send_message(call.message.chat.id, "Какая это нота?")

        button_nots = types.InlineKeyboardMarkup()
        button_do3 = types.InlineKeyboardButton(text="ДО", callback_data="DO3")
        button_re3 = types.InlineKeyboardButton(text="РЕ", callback_data="RE3")
        button_mi3 = types.InlineKeyboardButton(text="МИ", callback_data="MI3")
        button_fa3 = types.InlineKeyboardButton(text="ФА", callback_data="FA3")
        button_sol3 = types.InlineKeyboardButton(text="СОЛЬ", callback_data="SOL3")
        button_la3 = types.InlineKeyboardButton(text="ЛЯ", callback_data="LA3")
        button_si3 = types.InlineKeyboardButton(text="СИ", callback_data="SI3")


        button_nots.add(button_do3, button_re3, button_mi3, button_fa3,
                        button_sol3, button_la3, button_si3)
        bot.send_message(call.message.chat.id, "Выбери ноту", reply_markup=button_nots)


    elif call.data == "DO3":
        bot.send_message(call.message.chat.id, "Твой выбор")
        bot.send_photo(call.message.chat.id, do)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, full_card(cut_choise[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue3 = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont3")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue3, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "RE3":
        bot.send_message(call.message.chat.id, "Твой выбор")
        bot.send_photo(call.message.chat.id, re)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, full_card(cut_choise[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue3 = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont3")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue3, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "MI3":
        bot.send_message(call.message.chat.id, "Твой выбор")
        bot.send_photo(call.message.chat.id, mi)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, full_card(cut_choise[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue3 = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont3")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue3, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "FA3":
        bot.send_message(call.message.chat.id, "Твой выбор")
        bot.send_photo(call.message.chat.id, fa)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, full_card(cut_choise[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue3 = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont3")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue3, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "SOL3":
        bot.send_message(call.message.chat.id, "Твой выбор")
        bot.send_photo(call.message.chat.id, sol)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, full_card(cut_choise[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue3 = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont3")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue3, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "LA3":
        bot.send_message(call.message.chat.id, "Твой выбор")
        bot.send_photo(call.message.chat.id, la)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, full_card(cut_choise[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue3 = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont3")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue3, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

    elif call.data == "SI3":
        bot.send_message(call.message.chat.id, "Твой выбор")
        bot.send_photo(call.message.chat.id, si)
        bot.send_message(call.message.chat.id, "А вот правильный ответ")
        time.sleep(2)
        bot.send_photo(call.message.chat.id, full_card(cut_choise[-1]))

        button_continue_end = types.InlineKeyboardMarkup()
        button_continue3 = types.InlineKeyboardButton(text="Продолжить", callback_data="Cont3")
        button_end = types.InlineKeyboardButton(text="Закончить", callback_data="End")
        button_continue_end.add(button_continue3, button_end)
        bot.send_message(call.message.chat.id, "Продолжаем?", reply_markup=button_continue_end)

# игра 4 (финал)
    elif call.data == "game4":
        bot.send_photo(call.message.chat.id, muz_text)

        button_code_text = types.InlineKeyboardMarkup()
        button_code_1 = types.InlineKeyboardButton(text="Ля-ля-до-ля ре-ля-ми-ре", callback_data="first")
        button_code_2 = types.InlineKeyboardButton(text="фа-фа-ля-фа си-фа-ми-ре",callback_data="second")
        button_code_3 = types.InlineKeyboardButton(text="до-до-ми-до соль-до-ми-до", callback_data="third")
        button_code_4 = types.InlineKeyboardButton(text="фа-фа-ля-фа си-фа-ми-ре", callback_data="fourth")
        button_help_help = types.InlineKeyboardButton(text="Помощь нужна?", callback_data="help")



        button_code_text.add(button_code_1, button_code_2,button_code_3 ,button_code_4, button_help_help )
        bot.send_message(call.message.chat.id, "Посмотри на ноты в первом такте и Выбери подходящую расшифровку", reply_markup=button_code_text)
    elif call.data == "first":
        bot.send_message(call.message.chat.id, "Молодец!!Первый такт разгадан")
        bot.send_photo(call.message.chat.id, muz_text1)

        button_code_text_2 = types.InlineKeyboardMarkup()
        button_code_5 = types.InlineKeyboardButton(text="Ля-ля-до-ля ре-ля-ми-ре", callback_data="first1")
        button_code_6 = types.InlineKeyboardButton(text="фа-фа-ля-фа си-фа-ми-ре", callback_data="second1")
        button_code_7 = types.InlineKeyboardButton(text="до-до-ми-до соль-до-ми-до", callback_data="third1")
        button_code_8 = types.InlineKeyboardButton(text="фа-фа-ля-фа си-фа-ми-ре", callback_data="fourth1")

        button_code_text_2.add(button_code_5, button_code_6, button_code_7, button_code_8)
        bot.send_message(call.message.chat.id, "Разберёмся со 2-м тактом", reply_markup=button_code_text_2)
    elif call.data == "help":
        button_help = types.InlineKeyboardMarkup()
        button_help_1 = types.InlineKeyboardButton(text="Ноты 1 октавы", callback_data="help1")
        button_help_2 = types.InlineKeyboardButton(text="Ноты 2 октавы", callback_data="help2")
        button_help.add(button_help_1, button_help_2)
        bot.send_message(call.message.chat.id, "Помощь уже рядом", reply_markup=button_help)
    elif call.data == "first1":
        bot.send_message(call.message.chat.id, "Нет! попробуй ещё раз")

    elif call.data == "second1":
        bot.send_message(call.message.chat.id, "Ох! ((Это финал!(( Пробуй ещё! ")

    elif call.data == "third1":
        bot.send_message(call.message.chat.id, "Да!Да! Это верно")
        bot.send_message(call.message.chat.id, "Послушай и попробуй отгадать композицию))")
        bot.send_audio(call.message.chat.id, midi_file)

        button_name = types.InlineKeyboardMarkup()
        button_name1 = types.InlineKeyboardButton(text="из классики что-то", callback_data="lie")
        button_name2 = types.InlineKeyboardButton(text="из фильма", callback_data="true")
        button_name3 = types.InlineKeyboardButton(text="из попмузыки что-то", callback_data="lie")
        button_name.add(button_name1, button_name2, button_name3)
        bot.send_message(call.message.chat.id, "Что за музыка?", reply_markup=button_name)

    elif call.data == "lie":
        bot.send_message(call.message.chat.id, "Мимо!!!")

    elif call.data == "true":
        button_help = types.InlineKeyboardMarkup()
        button_audio = types.InlineKeyboardButton(text="слушать оригинал", callback_data="audio")
        button_practic = types.InlineKeyboardButton(text="сыграть самому", callback_data="practic")
        button_help.add(button_audio, button_practic)
        bot.send_message(call.message.chat.id, "Да!Да! Это верно", reply_markup=button_help)


    elif call.data == "practic":
        bot.send_message(call.message.chat.id, webbrowser.open(url))
    elif call.data == "audio":
        bot.send_audio(call.message.chat.id, music_file)

    elif call.data == "fourth1":
        button_help = types.InlineKeyboardMarkup()
        button_help_1 = types.InlineKeyboardButton(text="Ноты 1 октавы", callback_data="help1")
        button_help_2 = types.InlineKeyboardButton(text="Ноты 2 октавы", callback_data="help2")
        button_help.add(button_help_1, button_help_2)
        bot.send_message(call.message.chat.id, "Нет! Помощь уже рядом", reply_markup=button_help)

    elif call.data == "second":
        button_help = types.InlineKeyboardMarkup()
        button_help_1 = types.InlineKeyboardButton(text="Ноты 1 октавы", callback_data="help1")
        button_help_2 = types.InlineKeyboardButton(text="Ноты 2 октавы", callback_data="help2")
        button_help.add(button_help_1, button_help_2)

        bot.send_message(call.message.chat.id, "Нет! Помощь уже рядом", reply_markup=button_help)
    elif call.data == "third":
        button_help = types.InlineKeyboardMarkup()
        button_help_1 = types.InlineKeyboardButton(text="Ноты 1 октавы", callback_data="help1")
        button_help_2 = types.InlineKeyboardButton(text="Ноты 2 октавы", callback_data="help2")
        button_help.add(button_help_1, button_help_2)
        bot.send_message(call.message.chat.id, "Нет! Посмотри внимательнее((", reply_markup=button_help)




    elif call.data == "fourth":
        button_help = types.InlineKeyboardMarkup()
        button_help_1 = types.InlineKeyboardButton(text="Ноты 1 октавы", callback_data="help1")
        button_help_2 = types.InlineKeyboardButton(text="Ноты 2 октавы", callback_data="help2")
        button_help.add(button_help_1, button_help_2)
        bot.send_message(call.message.chat.id, "Помощь нужна?", reply_markup=button_help)
        bot.send_message(call.message.chat.id, "Нет! Посмотри внимательнее((", reply_markup=button_help)

    elif call.data == "help1":
        bot.send_photo(call.message.chat.id, help_1_oktava)
    elif call.data == "help2":
        bot.send_photo(call.message.chat.id, help_2_oktava)

bot.polling(none_stop=True)



