from datetime import datetime, date, timedelta

import requests
from celery import shared_task

from coursework_7_drf.settings import API_TG
from habits.models import Habit
from logger import setup_logger

logger = setup_logger()


def send_message(user_id, msg):
    """Отправка уведомления на телеграм"""
    params = {
        'chat_id': user_id,
        'text': msg
    }
    response = requests.post(f'https://api.telegram.org/bot{API_TG}/sendMessage', params=params)
    logger.info(f'Sent message to {response}')
    return response


@shared_task
def check_habit():
    now_hour = datetime.now().hour
    now_minute = datetime.now().minute
    now_date = date.today()
    habits = Habit.objects.all().filter(
        time__hour=now_hour, time__minute=now_minute, data_notification=now_date,
    )

    for habit in habits:
        logger.info(f'{habit.id}: {habit.time}')
        action = habit.action
        site = habit.site
        time = habit.time
        time_action = habit.time_complete
        user = habit.user.telegram_id
        period = habit.periodicity
        send_message(
            user, msg=f"я буду {action} в {time} в {site}. У вас {time_action} сек."
        )
        habit.data_notification = next_date_notification(period)
        habit.save()


def next_date_notification(period):
    """Возвращает дату следующего уведомления"""
    today = date.today()
    if period == '1':
        today = today + timedelta(days=1)
    elif period == '2':
        today = today + timedelta(days=2)
    elif period == '3':
        today = today + timedelta(days=3)
    elif period == '4':
        today = today + timedelta(days=4)
    elif period == '5':
        today = today + timedelta(days=5)
    elif period == '6':
        today = today + timedelta(days=6)
    elif period == '7':
        today = today + timedelta(days=7)
    else:
        today = None
    return today
