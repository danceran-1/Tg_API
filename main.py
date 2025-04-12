from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiogram import Bot, Dispatcher
from bot.handlers import router
from config.setting import API_TOKEN

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://yourcustomname.loca.lt{WEBHOOK_PATH}"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
dp.include_router(router)  

async def on_startup(app):
    """Устанавливаем webhook при старте приложения"""
    try:
        await bot.set_webhook(WEBHOOK_URL)
        print(f"Webhook установлен на {WEBHOOK_URL}")
    except Exception as e:
        print(f"Ошибка при установке вебхука: {e}")

async def on_shutdown(app):
    """Удаляем webhook при завершении работы приложения"""
    await bot.delete_webhook()
    print("Webhook удалён")

async def create_app():
    """Создание aiohttp приложения"""
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)


    app.router.add_post(WEBHOOK_PATH, SimpleRequestHandler(dispatcher=dp, bot=bot))

    app.router.add_post('/', handle)

    return app

async def handle(request):
    """Обработчик для вебхука"""
    try:
        data = await request.json() 
        print(f"Полученные данные: {data}")
        
        return web.Response(text="Данные получены и обработаны.")
    except Exception as e:
        return web.Response(text=f"Ошибка при обработке данных: {e}", status=500)

if __name__ == "__main__":
    web.run_app(create_app(), port=8080)
