from django.core.validators import MaxValueValidator
from django.db import models

from users.models import User


class Habit(models.Model):
    ONE = 'One'
    TWO = 'Two'
    THREE = 'Three'
    FOUR = 'Four'
    FIVE = 'Five'
    SIX = 'Six'
    SEVEN = 'Seven'
    PERIODICITY = {
        ONE: 'Ежедневно ',
        TWO: 'Один раз в два дня',
        THREE: 'Один раз в три дня',
        FOUR: 'Один раз в четыре дня',
        FIVE: 'Один раз в пять дня',
        SIX: 'Один раз в шесть дня',
        SEVEN: 'Один раз в неделю',
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    site = models.CharField(max_length=200, verbose_name='Место',
                            help_text='место, в котором необходимо выполнять привычку.')
    time = models.TimeField(verbose_name='Время', help_text='время, когда необходимо выполнять привычку.')
    action = models.CharField(max_length=300, verbose_name='действие',
                              help_text='действие, которое представляет собой привычка.')
    sign_pleasant_habit = models.BooleanField(
        verbose_name='Приятная привычка', default=False,
        help_text='привычка, которую можно привязать к выполнению полезной привычки.')
    related_habit = models.ManyToManyField('Habit', related_name='habit', blank=True, null=True,
                                           verbose_name='Связанные привычки')
    periodicity = models.CharField(max_length=5, choices=PERIODICITY, default=ONE)
    reward = models.CharField(max_length=300, verbose_name='Награда', help_text='Награда после выполнения привычки',
                              blank=True, null=True)
    time_complete = models.PositiveIntegerField(default=120, validators=[MaxValueValidator(120)],
                                                verbose_name='Время на выполнение привычки', )
    sign_publicity = models.BooleanField(default=False, verbose_name='Общедоступность',
                                         help_text='привычки можно публиковать в общий доступ')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
