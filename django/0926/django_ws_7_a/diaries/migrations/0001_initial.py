# Generated by Django 4.2.9 on 2024-09-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=125)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
