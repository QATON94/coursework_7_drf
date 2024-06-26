from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone

from coursework_7_drf.settings import AUTH_USER_MODEL


class Habit(models.Model):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    PERIODICITY = {
        ONE: 'Ежедневно ',
        TWO: 'Один раз в два дня',
        THREE: 'Один раз в три дня',
        FOUR: 'Один раз в четыре дня',
        FIVE: 'Один раз в пять дня',
        SIX: 'Один раз в шесть дня',
        SEVEN: 'Один раз в неделю',
    }

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True,
                             null=True)
    site = models.CharField(max_length=200, verbose_name='Место',
                            help_text='место, в котором необходимо выполнять привычку.')
    time = models.TimeField(verbose_name='Время', help_text='время, когда необходимо выполнять привычку.')
    action = models.CharField(max_length=300, verbose_name='действие',
                              help_text='действие, которое представляет собой привычка.')
    sign_pleasant_habit = models.BooleanField(
        verbose_name='Приятная привычка', default=True,
        help_text='привычка, которую можно привязать к выполнению полезной привычки.')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,
                                      null=True, verbose_name='Связанные привычки', default=None)
    periodicity = models.CharField(max_length=5, choices=PERIODICITY, default=ONE)
    reward = models.CharField(max_length=300, verbose_name='Награда', help_text='Награда после выполнения привычки',
                              blank=True, null=True, default=None)
    time_complete = models.PositiveIntegerField(default=120, validators=[MaxValueValidator(120)],
                                                verbose_name='Время на выполнение привычки', )
    sign_publicity = models.BooleanField(default=False, verbose_name='Общедоступность',
                                         help_text='привычки можно публиковать в общий доступ ')
    data_notification = models.DateField(default=timezone.now(), blank=True,
                                         verbose_name='Дата уведомления')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
