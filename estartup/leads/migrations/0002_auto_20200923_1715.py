# Generated by Django 3.0.7 on 2020-09-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(help_text='Введите адрес электронной почты', max_length=254, verbose_name='Электронная почта'),
        ),
    ]
