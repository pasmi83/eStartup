
from django.db import models

# Create your models here.
class ProjectImage(models.Model):
    title = models.CharField(max_length=20 ,blank = True,verbose_name="Название иллюстрации", help_text = "Лучше если название будет (поисковая оптимизация)")
    image = models.ImageField(blank = True,verbose_name="Иллюстрация", upload_to = 'project_image/')
    class Meta:
        verbose_name = "Иллюстрация"
        verbose_name_plural = "Иллюстрации"

class Project(models.Model):
    title = models.CharField(max_length=140, blank=False, help_text="Название проекта", verbose_name="Название")
    description = models.TextField(blank=True,verbose_name="Описание проекта", help_text="Годное описание проекта")
    is_active = models.BooleanField(verbose_name="Активность проекта", help_text="Есть ли набор на курс?")
    images = models.ManyToManyField(to = ProjectImage,verbose_name="Иллюстрации", help_text="Пусть лучше будут картинки")
    

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title
