from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Setup(models.Model):
    image_logo = models.ImageField(upload_to='image-logo/')
    email_list = ArrayField(models.EmailField(verbose_name= "Электронная почта",
    help_text="Введите адрес электронной почты",blank=False))

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"
        


