
from django.contrib import messages
from django.core.mail import send_mass_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from setup.models import Setup
from leads.models import Lead,Notification

def get_error_message_from_form(self, error):
    """берём конкретную ошибку из формы и преобразуем в message.error"""
    if len(error[1])>1:
        s_2 = 'были обнаружены следующие ошибки: '
    else:
        s_2 = 'была обнаружена ошибка - '
    error_message = 'В поле {} {} {}'.format(error[0],s_2,(', <br>').join(error[1]))  
    return messages.error(self.request, error_message)    
    

@receiver(post_save, sender = Lead)
def send_email_to_admin(instance,**kwargs):
    """получить экземпляр лида, и отправить администратору данные по почте"""
    subject = 'eStartup: сообщение от {} на тему "{}"'.format(getattr(instance,'name','Аноним'),getattr(instance,'subject','Без темы'))
    
    message = '{}. Номер для обратной связи: {}'.format(getattr(instance,'message','нет текста'),getattr(instance,'phone','не оставил'))
    
    from_email = getattr(instance,'email','анонимка') 
    
    recipient_list = Setup.objects.get(pk=1).email_list
    m = (subject,message,from_email,recipient_list)
    send_mass_mail((m,))

@receiver(post_save, sender = Lead)
def create_notification(instance,**kwargs):
    """создаёт Notification при создании Lead"""
    note = Notification(lead=instance)
    note.save()