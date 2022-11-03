from django.urls import include, path

from rest_framework import routers

from .views import CategoryViewSet, ProfileAPI, TransactionAPIView


router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)


urlpatterns = [
    # авторизация и регистрация c использованием токана
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # страница с транзакциями
    path('transition/', TransactionAPIView.as_view(), name='transaction'),
    # страница профиля
    path('profile/', ProfileAPI.as_view(), name='profile'),
    # регистрация роутеря для категорий
    path('', include(router.urls)),
]
