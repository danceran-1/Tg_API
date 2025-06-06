from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram import Bot, Dispatcher
from bot.handlers import router
from config.setting import API_TOKEN 


WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://mywebhooktest123.loca.lt{WEBHOOK_PATH}"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
dp.include_router(router)  

async def on_startup(app):
    """Устанавливаем webhook при старте приложения"""
    await bot.set_webhook(WEBHOOK_URL)
    print("Webhook установлен на", WEBHOOK_URL)

async def on_shutdown(app):
    """Удаляем webhook при завершении работы приложения"""
    await bot.delete_webhook()
    print("Webhook удалён")

async def create_app():
    """Создание aiohttp приложения"""
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

  
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)

   
    setup_application(app, dp, bot=bot)
    return app

if __name__ == "__main__":

    web.run_app(create_app(), port=8000)
