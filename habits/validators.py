from rest_framework import serializers

from habits.models import Habit


class NiceHabitValidator:
    def __call__(self, value):

        nice = dict(value).get('sign_pleasant_habit')
        related_habit = dict(value).get('related_habit')
        reward = dict(value).get('reward')

        if (nice and related_habit) or (nice and reward):
            raise serializers.ValidationError(
                'У приятной привычки не может быть вознаграждения или связанной привычки.'
            )
        elif related_habit and reward:
            raise serializers.ValidationError(
                'Нельзя одновременный выбирать связанные привычки и указывать вознаграждение'
            )


class RelatedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get(self.field)
        if related_habit and not related_habit.sign_pleasant_habit:
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки.')