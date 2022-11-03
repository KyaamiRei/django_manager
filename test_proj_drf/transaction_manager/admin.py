from django.contrib import admin

from .models import Category, Profile, Transaction


admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Profile)
