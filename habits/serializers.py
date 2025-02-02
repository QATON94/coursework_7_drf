from rest_framework import serializers

from habits.models import Habit
from habits.validators import NiceHabitValidator, RelatedHabitValidator


class HabitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HobitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [NiceHabitValidator(), RelatedHabitValidator(field='related_habit')]

    # def validate(self, data):
    #     if data['sign_pleasant_habit']:
    #         if data.get('related_habit'):
    #             raise serializers.ValidationError(
    #                 'У приятной привычки не может быть вознаграждения или связанной привычки.')
    #         elif data.get('reward'):
    #             raise serializers.ValidationError(
    #                 'У приятной привычки не может быть вознаграждения или связанной привычки.')
    #     elif data.get('related_habit'):
    #         if data.get('reward'):
    #             raise serializers.ValidationError(
    #                 'Нельзя одновременный выбирать связанные привычки и указывать вознаграждение')
    #     else:
    #         return data
