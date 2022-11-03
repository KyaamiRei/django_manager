from rest_framework import serializers

from .models import Category, Profile, Transaction


# сериализатор для транзакций
class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Transaction
        fields = ('__all__')


# сериализатор для категорий
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


# сериализатор для профиля
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')
