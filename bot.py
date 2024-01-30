import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import user_handler, other_handler
from configs.config import Config, load_config

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.INFO,
                        format='{filename}:{lineno} #{levelname:8} '
                        '[{asctime}] - {name} - {message}',
                        style='{')

    logger.info('Бот запустился')

    config: Config = load_config()

    bot = Bot(config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(user_handler.user_router)
    dp.include_router(other_handler.other_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
