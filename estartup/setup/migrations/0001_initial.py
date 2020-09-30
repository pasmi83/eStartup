# Generated by Django 3.0.7 on 2020-09-23 14:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_logo', models.ImageField(upload_to='image-logo/')),
                ('email_list', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(help_text='Введите адрес электронной почты', max_length=254, verbose_name='Электронная почта'), size=None)),
            ],
            options={
                'verbose_name': 'Настройки',
            },
        ),
    ]
