# Telegram Bot @jj_universitybot

## Описание
@jj_universitybot — это Telegram-бот, созданный для поднятия настроения с помощью шуток и предоставления возможности поддержать проект через донаты. Бот использует API `https://v2.jokeapi.dev/joke/Any` для получения шуток и отправляет изображение с ссылкой на донат при использовании команды `/link`.

## Возможности
- **/start**: Приветственное сообщение с описанием доступных команд.
- **/help**: Список доступных команд.
- **/random_joke**: Отправляет случайную шутку из API.
- **/link**: Отправляет изображение (`assets/bybit_wallet.png`) с ссылкой на поддержку проекта.

## Требования
- Python 3.10+
- Библиотеки:
  - `python-dotenv`
  - `aiohttp`
  - `aiogram`

## Установка
1. **Клонируйте репозиторий** (если применимо) или создайте файл `tg-bot-jj_universitybot.py` с кодом бота.

2. **Установите зависимости**:
   ```bash
   pip install python-dotenv aiohttp aiogram
   ```

3. **Создайте файл `.env`**:
   В корне проекта создайте файл `.env` с токеном бота:
   ```bash
   echo 'BOT_TOKEN=8262098685:AAEdNef2LN75ThgkQ6Bv6tQXks7x4CqjCSk' > .env
   ```
   Замените `8262098685:AAEdNef2LN75ThgkQ6Bv6tQXks7x4CqjCSk` на ваш токен от BotFather.

4. **Добавьте изображение**:
   - Создайте папку `assets`:
     ```bash
     mkdir assets
     ```
   - Поместите файл изображения `bybit_wallet.png` в папку `assets`. Например:
     ```bash
     mv /path/to/bybit_wallet.png assets/
     ```
     Убедитесь, что файл в формате PNG или JPEG.

5. **Добавьте `.env` в `.gitignore`**:
   ```bash
   echo '.env' >> .gitignore
   ```

## Запуск
1. Убедитесь, что файл `tg-bot-jj_universitybot.py`, `.env` и папка `assets` с изображением находятся в корне проекта.
2. Запустите скрипт:
   ```bash
   python tg-bot-jj_universitybot.py
   ```

## Команды
- `/start`: Показывает приветственное сообщение и список команд.
- `/help`: Описывает доступные команды (`/random_joke`, `/link`).
- `/random_joke`: Получает случайную шутку (однострочную или двухчастную) из API `https://v2.jokeapi.dev/joke/Any`.
- `/link`: Отправляет изображение `bybit_wallet.png` с подписью, содержащей ссылку на поддержку проекта (`https://www.tbank.ru/cf/7q5OpLNgOUc`).

## Структура проекта
```
project_folder/
├── tg-bot-jj_universitybot.py  # Основной скрипт бота
├── .env                        # Файл с токеном (не коммитить!)
├── assets/
│   ├── bybit_wallet.png        # Изображение для команды /link
├── .gitignore                  # Игнорирование .env
├── README.md                   # Этот файл
```

## Отладка
- Если команда `/random_joke` не работает:
  - Проверьте API:
    ```bash
    curl https://v2.jokeapi.dev/joke/Any
    ```
    Ожидаемый ответ — JSON с полями `type`, `joke` (для `single`) или `setup` и `delivery` (для `twopart`).
  - Проверьте логи в консоли для ошибок.
- Если команда `/link` не отправляет изображение:
  - Убедитесь, что `assets/bybit_wallet.png` существует и является изображением (PNG/JPEG).
- Если бот не запускается, проверьте, что `BOT_TOKEN` в `.env` корректен.

## Примечания
- Не коммитьте `.env` в репозиторий для безопасности токена.
- Убедитесь, что у вас стабильное интернет-соединение для работы с API.
- Если вы хотите изменить изображение или ссылку в `/link`, обновите `link` и `FSInputFile` в коде.

## Контакты
Для вопросов или предложений пишите создателю бота или используйте Telegram: @jj_universitybot.