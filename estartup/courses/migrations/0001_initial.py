# Generated by Django 3.0.7 on 2020-09-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Лучше если название будет (поисковая оптимизация)', max_length=20, verbose_name='Название иллюстрации')),
                ('image', models.ImageField(blank=True, upload_to='course_image/', verbose_name='Иллюстрация')),
            ],
            options={
                'verbose_name': 'Иллюстрация',
                'verbose_name_plural': 'Иллюстрации',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название курса', max_length=140, verbose_name='Название')),
                ('description', models.TextField(blank=True, help_text='Годное описание курса', verbose_name='Описание функции')),
                ('is_active', models.BooleanField(help_text='Есть ли набор на курс?', verbose_name='Активность курса')),
                ('images', models.ManyToManyField(help_text='Пусть лучше будут картинки', to='courses.CourseImage', verbose_name='Иллюстрации')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]