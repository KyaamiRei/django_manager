from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transaction_manager.urls')),  # подключение путей из нашего приложения
]
