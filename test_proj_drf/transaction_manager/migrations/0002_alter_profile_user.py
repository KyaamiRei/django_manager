# Generated by Django 4.1.3 on 2022-11-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.IntegerField(verbose_name='пользователь'),
        ),
    ]