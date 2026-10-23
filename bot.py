import telebot
from telebot import types

TOKEN = '8713387370:AAHk3FqN59G379HVfy95RIv1vEkoRav8USA'
bot = telebot.TeleBot(TOKEN)

# Функция генерации меню выбора областей обучения
def get_categories_keyboard(prefix):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_it = types.InlineKeyboardButton("💻 IT & Software", callback_data=f"{prefix}_it")
    btn_design = types.InlineKeyboardButton("🎨 UI/UX & Design", callback_data=f"{prefix}_design")
    btn_biz = types.InlineKeyboardButton("📊 Business & Marketing", callback_data=f"{prefix}_biz")
    btn_lang = types.InlineKeyboardButton("🌐 Languages & Science", callback_data=f"{prefix}_lang")
    btn_back = types.InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main_menu")
    
    markup.add(btn_it, btn_design, btn_biz, btn_lang)
    markup.add(btn_back)
    return markup

# Главное меню
def main_menu_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🎓 Free Courses", callback_data='courses_menu')
    btn2 = types.InlineKeyboardButton("💼 Internships", callback_data='internships_menu')
    btn3 = types.InlineKeyboardButton("🌍 Grants & Forums", callback_data='grants_menu')
    markup.add(btn1, btn2)
    markup.add(btn3)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 
        f"Hello, {message.from_user.first_name}! 👋\n\nWelcome to **Student Opportunity Hub**. This bot helps students discover free educational resources, internships, and international youth programs worldwide.",
        parse_mode='Markdown',
        reply_markup=main_menu_keyboard()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'main_menu':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Please select a category:",
            reply_markup=main_menu_keyboard()
        )

    elif call.data == 'courses_menu':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🎓 **Free Courses**\nChoose your field of study:",
            parse_mode='Markdown',
            reply_markup=get_categories_keyboard('course')
        )
    
    elif call.data == 'internships_menu':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="💼 **Internships & Career**\nChoose your field of study:",
            parse_mode='Markdown',
            reply_markup=get_categories_keyboard('intern')
        )

    # --- COURSES BY CATEGORY ---
    elif call.data == 'course_it':
        bot.send_message(call.message.chat.id, "💻 **IT & Software Courses:**\n1. [Stepik — Python & Databases](https://stepik.org)\n2. [CS50 — Harvard Introduction to Computer Science](https://cs50.harvard.edu)\n3. [FreeCodeCamp — Web Development Certification](https://freecodecamp.org)", parse_mode='Markdown')
    elif call.data == 'course_design':
        bot.send_message(call.message.chat.id, "🎨 **UI/UX & Design Courses:**\n1. [Coursera — Google UX Design Certificate](https://coursera.org)\n2. [Figma Academy — Web Design Essentials](https://figma.com)", parse_mode='Markdown')
    elif call.data == 'course_biz':
        bot.send_message(call.message.chat.id, "📊 **Business & Marketing Courses:**\n1. [Google Digital Garage — Fundamentals of Digital Marketing](https://learndigital.withgoogle.com)\n2. [HubSpot Academy — Inbound Marketing](https://academy.hubspot.com)", parse_mode='Markdown')
    elif call.data == 'course_lang':
        bot.send_message(call.message.chat.id, "🌐 **Languages & Science:**\n1. [British Council — IELTS Preparation](https://takeielts.britishcouncil.org)\n2. [Duolingo — Language Learning](https://duolingo.com)", parse_mode='Markdown')

    # --- INTERNSHIPS BY CATEGORY ---
    elif call.data == 'intern_it':
        bot.send_message(call.message.chat.id, "💼 **IT Internships:**\n1. Junior Frontend / Backend Remote Programs\n2. Data Analytics Virtual Internships", parse_mode='Markdown')
    elif call.data == 'intern_design':
        bot.send_message(call.message.chat.id, "💼 **Design Internships:**\n1. UI/UX Design Intern at Tech Startups\n2. Digital Media Creator Programs", parse_mode='Markdown')
    elif call.data == 'intern_biz':
        bot.send_message(call.message.chat.id, "💼 **Business & Startup Internships:**\n1. Business Development Associate\n2. SMM & Growth Marketing Intern", parse_mode='Markdown')
    elif call.data == 'intern_lang':
        bot.send_message(call.message.chat.id, "💼 **Languages & Content:**\n1. Content Translation & Localization Assistant\n2. Academic Peer Mentorship Programs", parse_mode='Markdown')

    # --- GRANTS & FORUMS ---
    elif call.data == 'grants_menu':
        bot.send_message(call.message.chat.id, "🌍 **Grants & International Forums:**\n1. [Youth Global Forum 2027 (Paris)](https://thecgdl.org/ygf2027)\n2. European Solidarity Corps (ESC) Volunteering\n3. International Youth Leadership Summits", parse_mode='Markdown')

# Кнопка связи / предложения
def main_menu_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🎓 Free Courses", callback_data='courses_menu')
    btn2 = types.InlineKeyboardButton("💼 Internships", callback_data='internships_menu')
    btn3 = types.InlineKeyboardButton("🌍 Grants & Forums", callback_data='grants_menu')
    btn4 = types.InlineKeyboardButton("💡 Suggest Opportunity", callback_data='suggest')
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    return markup

# Обработчик кнопки предложения
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # (ваш предыдущий код...)
    if call.data == 'suggest':
        bot.send_message(
            call.message.chat.id, 
            "💡 **Got an opportunity to share?**\nSend the link and short description to our email or contact the creator to help other students worldwide!",
            parse_mode='Markdown'
        )
        
bot.polling(none_stop=True)