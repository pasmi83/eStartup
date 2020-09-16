from django.db import models

# Create your models here.
class Announcement(models.Model):
    
    class Meta:      
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    title = models.CharField(max_length=60, blank = True,verbose_name="Заголовок объявления",
    help_text = "Лучше если заголовок будет (поисковая оптимизация)" )
    
    text = models.TextField(blank=False,verbose_name="Текст объявления",
    help_text = "Введите текст объявления")
    
    image = models.ImageField(upload_to = 'announcement_image/',
    default='default/default_tutor_image.png', verbose_name="Иллюстрация объявления",
    help_text="Пристойная иллюстрация") 
    
    is_active = models.BooleanField(default=True, verbose_name="Активность объявления",
    help_text = "Можно ли увидеть объявление")
    
    
    
    
    
    
    
    
    def __str__(self):
        return self.title
