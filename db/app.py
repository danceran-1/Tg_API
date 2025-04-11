from aiohttp import web
from bot.handlers import WebhookHandler  # Импортируем WebhookHandler
from container import Container  # Импортируем контейнер зависимостей

async def init_app():
    # Создаём контейнер зависимостей
    container = Container()

    # Получаем обработчик вебхуков с внедрённым PostRepository
    webhook_handler = container.webhook_handler()

    # Создаём приложение aiohttp
    app = web.Application()

    # Регистрируем маршрут для вебхука
    app.router.add_post('/webhook', webhook_handler.handle_webhook)

    return app

if __name__ == '__main__':
    # Инициализация aiohttp-приложения
    app = init_app()

    # Запуск веб-сервера
    web.run_app(app)
