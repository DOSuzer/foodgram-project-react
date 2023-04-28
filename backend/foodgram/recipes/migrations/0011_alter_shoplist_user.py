# Generated by Django 3.2 on 2023-04-28 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0010_alter_favorite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoplist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoplist', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
