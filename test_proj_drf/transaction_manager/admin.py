from django.contrib import admin

from .models import Category, Profile, Transaction


# регистрация компонентов в панели администрации
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Profile)
