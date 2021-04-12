from django.db import models
import datetime
# Create your models here.


class Review(models.Model):
    author = models.CharField('Автор', max_length=50)
    category = models.CharField('Категория', max_length=50)
    text = models.TextField('Текст отзыва')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'