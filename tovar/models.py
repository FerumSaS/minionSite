from django.core.exceptions import ValidationError
from django.db import models
from taggit.managers import TaggableManager


class TovarCreate(models.Model):
    cover = models.ImageField('Основное фото', upload_to='main/static/main/img')
    title = models.CharField('Название', max_length=50)
    category = models.CharField('Категория', max_length=16, default='Null', choices=(
        ('Ordinary', 'Обычные'),
        ('Collection', 'Коллекционные'),
        ('Popular', 'Популярные'),
    ))
    short_description = models.CharField('Краткое описание', max_length=250, blank=True)
    description = models.TextField('Описание')
    tags = TaggableManager(verbose_name='Новые теги', blank=True, help_text='Введите теги через запятую с большой буквы, без пробелов')

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()

        if self.category == 'Popular':
            popular_count = TovarCreate.objects.filter(category='Popular').count()
            if popular_count >= 6:
                raise ValidationError('Превышено максимальное количество товаров в категории "Популярные"')
        if self.category == 'Collection':
            collection_count = TovarCreate.objects.filter(category='Collection').count()
            if collection_count >= 3:
                raise ValidationError('Превышено максимальное количество товаров в категории "Коллекционные"')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Image(models.Model):
    article = models.ForeignKey(TovarCreate, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Изображения:', upload_to='main/static/main/img')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Дополнительные изображения'


class Carousel(models.Model):
    title = models.CharField('Название', max_length=50)
    photo = models.ImageField('Фото', upload_to='main/static/main/img')

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = 'Изображение для карусели'
        verbose_name_plural = 'Изображения для карусели'



