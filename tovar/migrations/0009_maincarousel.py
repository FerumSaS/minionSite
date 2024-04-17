# Generated by Django 4.0.5 on 2023-07-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tovar', '0008_carousel_is_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='main/static/main/img', verbose_name='Основное фото')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Карусель Главная',
                'verbose_name_plural': 'Карусель фоток на главной',
            },
        ),
    ]