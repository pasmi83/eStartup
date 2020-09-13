from django.db import models

# Create your models here.
class Feedback(models.Model):
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


    title = models.CharField(max_length=60, blank = True,verbose_name="Заголовок",
    help_text = "Лучше если заголовок будет (поисковая оптимизация)" )

    description = models.TextField(blank=False,verbose_name="Текст отзыва",
    help_text = "Введите текст отзыва")

    created_at = models.DateTimeField(auto_now_add = True, verbose_name="Дата создания",
    help_text = "Когда добавлен отзыв")

    ﬁrst_name = models.CharField(max_length=40 ,blank=False, verbose_name="Имя",
    help_text = "Введите ваше имя")

    last_name = models.CharField(max_length=40 ,blank=False, verbose_name="Фамилия",
    help_text = "Введите вашу фамилию")

    is_active = models.BooleanField(default=True, verbose_name="Активность отзыва",
     help_text="Можно ли увидеть отзыв")

    def __str__(self):
        return """{} {} '{}' """.format(self.first_name, self.last_name,self.title)
