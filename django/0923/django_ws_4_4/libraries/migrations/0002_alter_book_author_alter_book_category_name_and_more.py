# Generated by Django 4.2.2 on 2024-09-23 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='category_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(),
        ),
    ]