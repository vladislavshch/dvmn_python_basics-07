import ptbot
import os
from dotenv import load_dotenv
from pathlib import Path
from pytimeparse import parse


def wait(chat_id, question):
    message_id = bot.send_message(chat_id, "Запускаю таймер.....")
    bot.create_countdown(parse(question), notify_progress, chat_id=chat_id, message_id=message_id, total_seconds=parse(question))
    bot.create_timer(parse(question), choice, author_id=chat_id, message=question)


def notify_progress(secs_left, chat_id, message_id, total_seconds):
    iteration = total_seconds - secs_left
    bot.update_message(chat_id, message_id,f"Осталось {secs_left} секунд! \n{render_progressbar(total_seconds, iteration)}")


def choice(author_id):
    bot_message = "Время вышло"
    bot.send_message(author_id, bot_message)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return "{0} |{1}| {2}% {3}".format(prefix, pbar, percent, suffix)


def main():
    bot.reply_on_message(wait)
    bot.run_bot()


if __name__ == "__main__":
    env_path = Path(".") / " .env"
    load_dotenv(dotenv_path=env_path)
    telegram_token = os.getenv("TG_TOKEN")
    telegram_chat_id = os.getenv("TG_CHAT_ID")
    bot = ptbot.Bot(telegram_token)
    main()

