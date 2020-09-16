from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class CourseImage(models.Model):
    class Meta:
        verbose_name = "Иллюстрация"
        verbose_name_plural = "Иллюстрации"

    title = models.CharField(max_length=20 ,blank = True,verbose_name="Название иллюстрации",
     help_text = "Лучше если название будет (поисковая оптимизация)")

    image = models.ImageField(blank = True,
    verbose_name="Иллюстрация", upload_to = 'course_image/' )

    def __str__(self):
        return '{} {}'.format(self.image.name.split('/')[-1],self.title)

    

class Course(models.Model):
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    title = models.CharField(max_length=140, blank=False,
     help_text="Название курса", verbose_name="Название")

    description = models.TextField(blank=True,verbose_name="Описание курса",
     help_text="Годное описание курса")

    is_active = models.BooleanField(verbose_name="Активность курса", 
    help_text="Есть ли набор на курс?")

    images = models.ManyToManyField(to = CourseImage,verbose_name="Иллюстрации", 
    help_text="Пусть лучше будут картинки")

    lesson_list =ArrayField(
        models.CharField(max_length=140,null=True, verbose_name="Тема урока")
        ,null=True,blank = True,verbose_name="Список уроков",default=list
        ) 

    def __str__(self):
        return self.title

class CourseAdvantage(models.Model):
    class Meta:
        verbose_name = "Приемущество"
        verbose_name_plural = "Приемущества"
    

    title = models.CharField(max_length=140, blank=False, 
    help_text="Название приемущества курса", verbose_name="Название")

    description = models.TextField(blank=True,verbose_name="Описание приемущества курса",
     help_text="Годное описание приемущества курса")

    is_active = models.BooleanField(verbose_name="Активность приемущества курса", 
    help_text="Есть ли набор на курс?")

    image = models.ImageField(blank = False,verbose_name="Иллюстрация", 
    upload_to = 'advantage_image/' )







