# Generated by Django 3.2.7 on 2023-02-07 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='категории')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(verbose_name='Дата окончание')),
                ('image', models.ImageField(upload_to='todo/image/', verbose_name='Картинки')),
                ('is_done', models.BooleanField(default=False, verbose_name='Готово ли?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todoes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]