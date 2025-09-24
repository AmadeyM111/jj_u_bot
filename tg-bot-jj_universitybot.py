import asyncio
import re
import aiohttp
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile

# Загружаем переменные окружения из .env файла
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN") # token of the bot

dp = Dispatcher()

@dp.message(CommandStart()) # для обозначения команды мы добавляем декоратор @ для изменения фукции кода, не меняя его самого
async def start_command_handler(message: Message) -> None: # сообщение пользователя это больше, чем текст, там хранится и идентификатор пользователя, его имя и еще много чего
#    await message.answer("Привет! Я бот, который поможет тебе с покупкой и продажей криптовалюты на ByBit!") # останавливаем выполнение функции до тех пор, пока операция не закончит работу 
    await message.answer("Привет! Я бот, который поможет поднять тебе настроение, отборными шутками!") # останавливаем выполнение функции до тех пор, пока операция не закончит работу 
    await message.answer("Напиши мне /help, чтобы узнать, что я могу сделать.")

@dp.message(Command('help')) # для обозначения команды мы добавляем декоратор @ для изменения фукции кода, не меняя его самого
async def help_command_handler(message: Message) -> None: # сообщение пользователя это больше, чем текст, там хранится и идентификатор пользователя, его имя и еще много чего
    await message.answer("Ты можешь поднять себе настроение, написав команду /random_joke!") 

@dp.message(Command('random_joke')) # для обозначения команды мы добавляем декоратор @ для изменения фукции кода, не меняя его самого
async def start_joke_handler(message: Message) -> None: # удаление не-ASCII символов, чтобы Telegram корректно отобразил текст

    try:
        async with aiohttp.ClientSession() as session: # сообщение пользователя это больше, чем текст, там хранится и идентификатор пользователя, его имя и еще много чего
            async with session.get("https://v2.jokeapi.dev/joke/Any") as response:
                if response.status != 200:
                    await message.answer("Ошибка при получении шутки. Попробуйте позже.")
                    return
                content_type = response.headers.get('Content-Type', '')
                if 'application/json' not in content_type:
                    await message.answer("Ошибка: API вернул неверный формат данных (не JSON).")
                    return
                contents = await response.json()

                if contents.get('type') == 'single':
                    joke = contents.get('joke', '')
                else:
                    setup = contents.get('setup', '')
                    delivery = contents.get('delivery', '')
                    joke = f"{setup}\n{delivery}" if setup and delivery else ''
                if not joke:
                    await message.answer("Шутка не нашлась.")
                    return 
                # Нормализация текста - обработка некоректных символов
                joke = joke.encode('utf-8', errors='ignore').decode('utf-8')
                joke = re.sub(r'[^\x00-\x7F]+', '', joke) # 

                print(f"Полученная шутка: {joke}")
                await message.answer(joke)
                await message.answer(f"При желании, вы можете оказать поддержку развитию проекта, нажав команду /thanks")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {str(e)}")
        print(f"Ошибка в random_joke: {e}")


@dp.message(Command('thanks'))
async def thanks_handler(message: Message) -> None:
    # Ссылки на донат
    thanks = "https://www.tbank.ru/cf/7q5OpLNgOUc"
    photo = FSInputFile("assets/bybit_wallet.png")
    await message.answer_photo(
        photo=photo,
        caption=f"При желании, вы можете оказать поддержку развитию проекта: {thanks}"
    )

async def main() -> None: 
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 