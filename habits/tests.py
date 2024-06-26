from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class MaterialsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru', telegram_id=866009530, is_active=True)
        self.habit = Habit.objects.create(user=self.user, site='Улица', time='08:00', action='Выпить кофе',
                                          sign_pleasant_habit=False, related_habit=None, periodicity='1',
                                          reward=None, time_complete=120, sign_publicity=True)
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse('habits:habits-view', args=(self.habit.id,))
        response = self.client.get(url)
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['reward'], self.habit.reward)

    def test_habit_create(self):
        url = reverse('habits:habits-create')
        data = {
            'site': 'Улица', 'time': '08:00', 'action': 'Сделать зарядку',
            'sign_pleasant_habit': False, 'related_habit': 1, 'periodicity': '1',
            'time_complete': 120, 'sign_publicity': True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_update(self):
        url = reverse('habits:habits-update', args=(self.habit.id,))
        data = {
            'site': 'Дом',
        }
        response = self.client.patch(url, data)
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('site'), 'Дом')

    def test_habit_list(self):
        url = reverse('habits:habits-list')
        response = self.client.get(url)
        response_data = response.data
        result = {'count': 1, 'next': None, 'previous': None, "results": [
            {'id': 4, 'site': 'Улица', 'time': '08:00:00', 'action': 'Выпить кофе', 'sign_pleasant_habit': False,
             'periodicity': '1', 'reward': None, 'time_complete': 120, 'sign_publicity': True,
             'data_notification': date.today().strftime('%Y-%m-%d'), 'user': 3, 'related_habit': None}]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, result)

    def test_habit_validate_time_complete(self):
        url = reverse('habits:habits-create')
        data = {
            'site': 'Улица', 'time': '08:00', 'action': 'Сделать зарядку',
            'sign_pleasant_habit': False, 'related_habit': self.habit.id, 'periodicity': '1',
            'time_complete': 1200, 'sign_publicity': True,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.json(), {'time_complete': ['Ensure this value is less than or equal to 120.']})

    def test_habit_validate_sign_pleasant_habit(self):
        url = reverse('habits:habits-create')
        data = {
            'site': 'Улица', 'time': '08:00', 'action': 'Сделать зарядку',
            'sign_pleasant_habit': True, 'related_habit': self.habit.id, 'periodicity': '1',
            'time_complete': 120, 'sign_publicity': True,
        }
        response = self.client.post(url, data)
        response_data = response.json()
        self.assertEqual(response_data['non_field_errors'][0],
                         'У приятной привычки не может быть вознаграждения или связанной привычки.')

    def test_habit_validate_related_habit(self):
        url = reverse('habits:habits-create')
        data = {
            'site': 'Улица', 'time': '08:00', 'action': 'Сделать зарядку',
            'sign_pleasant_habit': False, 'related_habit': self.habit.id, 'periodicity': '1',
            'time_complete': 120, 'sign_publicity': True, 'reward': 'Награда'
        }
        response = self.client.post(url, data)
        response_data = response.json()
        self.assertEqual(response_data['non_field_errors'][0],
                         'Нельзя одновременный выбирать связанные привычки и указывать вознаграждение')

    def test_habit_delete(self):
        url = reverse('habits:habits-delete', args=(self.habit.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_user_create(self):
        url = reverse('users:register')
        response = self.client.post(url, {'email': 'new_user@mail.ru', 'password': '123qwe', 'telegram_id': '123456789'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.data['email'], 'new_user@mail.ru')
