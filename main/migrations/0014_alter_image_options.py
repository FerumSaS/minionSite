# Generated by Django 4.0.5 on 2023-03-12 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_articles_cover_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Дополнительные изображения'},
        ),
    ]