from django.urls import include, path

from rest_framework import routers

from .views import CategoryViewSet, ProfileAPI, TransactionAPIView


# роутер для более удобного использования ViewSets
router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)


# пути используемые в приложении
urlpatterns = [
    # авторизация и регистрация c использованием токана
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('rest-auth/', include('rest_framework.urls')),
    # страница с транзакциями
    path('transition/', TransactionAPIView.as_view(), name='transaction'),
    # страница профиля
    path('profile/', ProfileAPI.as_view(), name='profile'),
    # регистрация роутеря для категорий
    path('', include(router.urls)),
]
