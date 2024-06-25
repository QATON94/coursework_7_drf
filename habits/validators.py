# from rest_framework import serializers
#
#
# class ValidatorHabits:
#
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value):
#         data = dict(value).get(self.field)
#         print(data)
#         if data['sign_pleasant_habit']:
#             if data.get('related_habit'):
#                 raise serializers.ValidationError(
#                     'У приятной привычки не может быть вознаграждения или связанной привычки.')
#             elif data.get('reward'):
#                 raise serializers.ValidationError(
#                     'У приятной привычки не может быть вознаграждения или связанной привычки.')
#         elif data.get('related_habit'):
#             if data.get('reward'):
#                 raise serializers.ValidationError(
#                     'Нельзя одновременный выбирать связанные привычки и указывать вознаграждение')
