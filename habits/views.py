from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import CustomPaginator
from habits.serializers import HabitListSerializer, HabitSerializer, HobitCreateSerializer
from users.permissions import IsOwner


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitListSerializer
    permission_classes = [IsOwner]
    pagination_class = CustomPaginator

    def get_queryset(self):
        return Habit.objects.filter(
            Q(sign_publicity=True) | Q(user=self.request.user)
        ).distinct()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Habit.objects.all().filter(sign_publicity=True, id=self.kwargs['pk'])
        if queryset.exists():
            return queryset
        else:
            queryset = Habit.objects.all().filter(user=self.request.user)
        return queryset


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HobitCreateSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
