from aiogram.types import ReplyKeyboardMarkup , KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button1 = KeyboardButton(text='Выбор')
button2 = KeyboardButton(text='Еще что-то')
button_text = "Поулчить инофрмацию"



get_api = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Получить данные", callback_data="get_data")]
])

seting = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=button_text, url="https://belgorod.hh.ru/vacancy/119161743?hhtmFrom=chat")
    ]
])