# Generated by Django 3.0.7 on 2020-09-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='biography',
            field=models.TextField(blank=True, help_text='Биографические сведенья', verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='first_name',
            field=models.CharField(help_text='Имя преподавателя', max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='image',
            field=models.ImageField(default='default/default_tutor_image.png', help_text='Пристойное изображение', upload_to='tutor_image/', verbose_name='Портрет'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='is_active',
            field=models.BooleanField(help_text='Активна ли запись', verbose_name='Активность записи'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='last_name',
            field=models.CharField(blank=True, help_text='Фамилия преподавателя', max_length=20, verbose_name='Фамилия'),
        ),
    ]