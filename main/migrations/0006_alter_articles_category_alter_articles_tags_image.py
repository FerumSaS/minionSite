# Generated by Django 4.1.7 on 2023-03-01 17:03

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('main', '0005_alter_articles_cover_alter_articles_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(
                choices=[('Null', '---------'), ('Set', 'Набор'), ('Collection', 'Коллекционные'), ('Series', 'Серия')],
                default='Null', max_length=16, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='tags',
            field=taggit.managers.TaggableManager(
                help_text='Введите теги через запятую или выберите из уже существующих', through='taggit.TaggedItem',
                to='taggit.Tag', verbose_name='Теги'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images',
                                              to='main.articles')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
