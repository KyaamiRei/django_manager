from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Category, Profile, Transaction
from .serializers import CategorySerializer, ProfileSerializer, TransactionSerializer


# представление для вывода списка транзакций
class TransactionAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)


# представление для работы с категориями
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


# представление для вывода списка транзакций
class ProfileAPI(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
