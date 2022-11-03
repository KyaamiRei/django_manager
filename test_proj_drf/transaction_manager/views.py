from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Category, Profile, Transaction
from .serializers import CategorySerializer, ProfileSerializer, TransactionSerializer


# параметры для сортировки
filter_params = False  # поле даты создания или цена
filter_order = True  # сортировка по убываю или возрастания


# изменение состояния сортировки
def set_filter_params(filter_params):
    filter_params = not filter_params
    return filter_params


# изменение состояния сортировки
def set_order(filter_order):
    filter_order = not filter_order
    return filter_order


# представление для вывода списка транзакций
class TransactionAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Transaction.objects.order_by(('', '-')[filter_order] + ('price', 'time_create')[filter_params])


# представление для работы с категориями
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    # добавление категорий в список, если список пуст
    cat_list = [
        "Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина", "Образование",
        "Отдых и развлечения", "Платежи, комиссии", "Покупки: одежда, техника", "Продукты", "Проезд",
    ]

    if not queryset:
        for item in cat_list:
            Category.objects.create(name=item)


# представление для вывода списка транзакций
class ProfileAPI(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
