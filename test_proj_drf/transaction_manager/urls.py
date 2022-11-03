from django.urls import path

from .views import CategoryAPIUpdate, CategoryAPIView, TransactionAPIView

urlpatterns = [
    # страница с транзакциями
    path('transactionList//', TransactionAPIView.as_view(), name='transactionList'),
    # страница с категориями
    path('categoryList', CategoryAPIView.as_view(), name='catList'),
    # страница редактирования категорий
    path('categoryList/<int:pk>/', CategoryAPIUpdate.as_view(), name='catListUpdate'),
]
