# Generated by Django 4.0.5 on 2023-03-01 23:33

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_articles_tag_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tag_field',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Миньоны', 'Миньоны'), ('НеМиньоны', 'НеМиньоны'), ('КтоТо', 'КтоТо'), ('FSPшники', 'FSPшники')], max_length=32),
        ),
    ]