from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import bot.keybords as kb
from db.database import PostRepository, async_session, init_db
from db.database import PostDB
from utils.myApi import get_data_from_api
from injector import inject

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    """При нажатии на Start"""
    await message.reply("Нажми кнопку, чтобы получить информацию!", reply_markup=kb.get_api)

@router.message(Command('help'))
async def help(message: Message):
    """При нажатии на help"""
    await message.answer("Help", reply_markup=kb.seting)

@router.callback_query(lambda c: c.data == "get_data")
async def get_data(callback: CallbackQuery):
    """Получаем информацию по апи"""
    await init_db()
    await callback.answer("Запрашиваю данные...")
    try:
        data = await get_data_from_api()
        if not data or not data.root:
            await callback.message.answer("Нет данных для сохранения.")
            return

        posts_data = [post.model_dump() for post in data.root]
        posts_objects = [PostDB(**data) for data in posts_data]

        async with async_session() as session:
            repo = PostRepository(session)
            await repo.save_all(posts_objects)

        await callback.message.answer("Данные были успешно сохранены")
    
    except Exception as e:
        await callback.message.answer(f"Ошибка при получении данных: {e}")
