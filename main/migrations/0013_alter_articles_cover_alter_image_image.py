# Generated by Django 4.0.5 on 2023-03-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_articles_tag_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='cover',
            field=models.ImageField(upload_to='main/static/main/img', verbose_name='Основное фото'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='main/static/main/img', verbose_name='Изображения:'),
        ),
    ]