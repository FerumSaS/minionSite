# Generated by Django 4.0.5 on 2023-03-07 19:58

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_articles_tag_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='tag_field',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('миньоны', 'Миньоны'), ('неминьоны', 'НеМиньоны'), ('ктото', 'КтоТо'), ('fspшники', 'FSPшники'), ('гдето', 'ГдеТо'), ('комуто', 'КомуТо')], default=0, max_length=45, verbose_name='Существующие Теги'),
            preserve_default=False,
        ),
    ]
