import datetime

from django.core.mail import send_mail

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Category, Profile, Transaction
from .serializers import CategorySerializer, ProfileSerializer, TransactionSerializer


# параметры для сортировки
filter_params = True  # поле даты создания или цена
filter_order = False  # сортировка по убываю или возрастания


# изменение состояния сортировки
def set_filter_params(filter_params):
    filter_params = not filter_params
    return filter_params


# изменение состояния сортировки
def set_order(filter_order):
    filter_order = not filter_order
    return filter_order


# отправка письсма на почту пользователя
def send_statistics(user_id):
    datetime_now = datetime.datetime.now().time
    send_time = datetime.time(9, 00, 00)  # отправка производится в 9 утра
    if datetime_now == send_time:
        queryset = Profile.objects.filter(user=user_id)
        for item in queryset:
            total_money = item.user_balance
            continue
        # отправка письма
        mail = send_mail(
            "Статистика расходов", f"За период пользования приложения вы потратили {total_money} руб.",
            'kolyavasilenko2703@mail.ru', ['lulnyyk@mail.ru'], fail_silently=True,
        )
        if mail:
            print('Письмо отправлено')
        else:
            print('Ошибка отправки1')


# представление для вывода списка транзакций
class TransactionAPIView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user.id)
        return queryset.order_by(('', '-')[filter_order] + ('price', 'time_create')[filter_params])


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
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    # получение профиля пользовате, расчет его транзакций и  отправка на почту отчета
    def get_queryset(self):
        queryset = Profile.objects.filter(user=self.request.user.id)

        if not queryset:
            Profile.objects.create(user=self.request.user.id, user_email="qqq@mail.ru", user_balance=0)
            queryset = Profile.objects.filter(user=self.request.user.id)
        else:
            queryset_transaction = Transaction.objects.filter(user=self.request.user.id)
            total_price = 0
            for item in queryset_transaction:
                total_price += item.price
                for item in queryset:
                    item.user_balance = total_price
                    item.save()

        send_statistics(self.request.user.id)

        return queryset
