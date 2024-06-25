from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitRetrieveAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habits-list'),
    path('view/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits-view'),
    path('create/', HabitCreateAPIView.as_view(), name='habits-create'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habits-update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habits-delete'),
]