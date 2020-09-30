from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Lead(models.Model):

    class Meta:
        verbose_name = "Холодный контакт"
        verbose_name_plural = "Холодные контакты"

    name =  models.CharField(blank = False, max_length=40,verbose_name='Имя отправителя',
    help_text="Введите ваше имя.")

    phone = PhoneNumberField(verbose_name='Телефонный номер',
    help_text="Введите телефонный номер",blank=True)

    email = models.EmailField(verbose_name='Электронная почта',
    help_text="Введите адрес электронной почты",blank=False)

    subject = models.CharField(max_length=60, verbose_name='Тема сообщения',
    help_text="Кратко опишите суть",blank=False) 

    message = models.TextField(verbose_name='Текст сообщения',
    help_text="Развёрнуто опишите вопрос",blank=True)
    
    """def notifications_count(self,verbose_name='Количество ответов',):
        
        return Notification.objects.filter(lead=self).count()"""
    def __str__(self):
        return '{} от {}'.format(self.subject, self.name)


class Notification(models.Model):

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return 'Ответ {} по теме  "{}"'.format(self.lead.name,self.lead.subject)

    lead = models.ForeignKey('Lead',on_delete = models.DO_NOTHING,)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    status = models.CharField(choices=(('0','новое'),('1','в процессе'),('2','завершено')),
    default='0',verbose_name='Статус',max_length=1)

    is_done = models.BooleanField(default= False, verbose_name = 'Завершено')
    
    notice = models.TextField(verbose_name = 'Текст сообщения')


