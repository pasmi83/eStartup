from django.db import models

class Tutor(models.Model):

    ﬁrst_name=models.CharField(max_length=20,help_text="Имя преподавателя", blank=False, verbose_name = "Имя")
    last_name=models.CharField(max_length=20,help_text="Фамилия преподавателя", blank = True, verbose_name = "Фамилия")
    biography=models.TextField(blank=True,help_text="Биографические сведенья", verbose_name = "Биография")
    image=models.ImageField(upload_to = 'tutor_image/',default='default/default_tutor_image.png', verbose_name="Портрет", help_text="Пристойное изображение")
    is_active=models.BooleanField(help_text="Активна ли запись", verbose_name = "Активность записи" )

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        

    def __str__(self):
        return '{} {} with ID:{}'.format(self.last_name, self.first_name, self.pk)
