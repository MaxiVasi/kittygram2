from rest_framework import viewsets

from .models import Achievement, Cat, User

from .serializers import AchievementSerializer, CatSerializer, UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    # Новая запись в БД создаётся при вызове метода save() сериализатора,
    # а этот метод вызывается из метода вьюсета perform_create().
    # Cериализатор не ожидает id пользователя в POST-запросе (или игнорирует
    # его при получении), а при создании записи о новом котике в БД
    # информация о пользователе берётся из объекта request.user.
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
