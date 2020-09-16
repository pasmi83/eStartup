from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Lead(models.Model):

    class Meta:
        verbose_name = "Холодный контакт"
        verbose_name_plural = "Холодные контакты"

    name =  models.CharField(blank = False, max_length=40,verbose_name='Имя',
    help_text="Введите ваше имя.")

    phone = PhoneNumberField(verbose_name='Телефонный номер',
    help_text="Введите телефонный номер",blank=True)

    email = models.EmailField(verbose_name='Электронная почта',
    help_text="Введите телефонный номер",blank=False)

    subject = models.CharField(max_length=60, verbose_name='Тема сообщения',
    help_text="Кратко опишите суть",blank=False) 

    message = models.TextField(verbose_name='Текст сообщения',
    help_text="Развёрнуто опишите вопрос",blank=True)
    
    def __str__(self):
        return '{} от {}'.format(self.subject, self.name) 
