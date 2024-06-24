# Generated by Django 5.0.6 on 2024-06-24 12:59

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(help_text='место, в котором необходимо выполнять привычку.', max_length=200, verbose_name='Место')),
                ('time', models.TimeField(help_text='время, когда необходимо выполнять привычку.', verbose_name='Время')),
                ('action', models.CharField(help_text='действие, которое представляет собой привычка.', max_length=300, verbose_name='действие')),
                ('sign_pleasant_habit', models.BooleanField(default=False, help_text='привычка, которую можно привязать к выполнению полезной привычки.', verbose_name='Приятная привычка')),
                ('periodicity', models.CharField(choices=[('One', 'Ежедневно '), ('Two', 'Один раз в два дня'), ('Three', 'Один раз в три дня'), ('Four', 'Один раз в четыре дня'), ('Five', 'Один раз в пять дня'), ('Six', 'Один раз в шесть дня'), ('Seven', 'Один раз в неделю')], default='One', max_length=5)),
                ('reward', models.CharField(blank=True, help_text='Награда после выполнения привычки', max_length=300, null=True, verbose_name='Награда')),
                ('time_complete', models.PositiveIntegerField(default=120, validators=[django.core.validators.MaxValueValidator(120)], verbose_name='Время на выполнение привычки')),
                ('sign_publicity', models.BooleanField(default=False, help_text='привычки можно публиковать в общий доступ', verbose_name='Общедоступность')),
                ('related_habit', models.ManyToManyField(blank=True, null=True, related_name='habit', to='habits.habit', verbose_name='Связанные привычки')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
