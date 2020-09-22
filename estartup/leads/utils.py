
from django.contrib import messages
import json

def get_error_message_from_form(self, error):
    if len(error[1])>1:
        s_2 = 'были обнаружены следующие ошибки: '
    else:
        s_2 = 'была обнаружена ошибка - '
    error_message = 'В поле {} {} {}'.format(error[0],s_2,(', <br>').join(error[1]))  
    return messages.error(self.request, error_message)    
    