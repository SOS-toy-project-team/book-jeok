# Generated by Django 4.1.6 on 2023-02-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=10, unique=True)),
                ('user_id', models.CharField(default='', max_length=10, unique=True)),
                ('user_pw', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
