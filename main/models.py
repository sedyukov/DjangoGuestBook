from django.db import models
import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField('Категория', max_length=50)

    def __str__(self):
        return self.name


class ReviewOld(models.Model):
    author = models.CharField('Автор', max_length=50)
    category = models.CharField('Категория', max_length=50)
    date = models.DateField('Дата добавления', auto_now_add=True)
    time = models.TimeField('Время обращения', auto_now_add=True)
    text = models.TextField('Текст отзыва')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Review(models.Model):
    author = models.CharField('Автор', max_length=50)
    #category = models.ManyToOneRel('Категории', Category, 'Категория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField('Дата добавления', auto_now_add=True)
    time = models.TimeField('Время обращения', auto_now_add=True)
    text = models.TextField('Текст отзыва')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'