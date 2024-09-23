# Generated by Django 4.2.2 on 2024-09-23 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=10)),
                ('isbn13', models.CharField(max_length=13)),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('price', models.IntegerField()),
                ('publisher', models.CharField(max_length=100)),
                ('fixed_price', models.BooleanField(default=False)),
                ('pub_date', models.DateField()),
                ('link', models.URLField()),
                ('adult', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.IntegerField()),
            ],
        ),
    ]
