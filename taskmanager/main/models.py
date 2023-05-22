from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class newTask(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    creation_date = models.DateField('Дата создания', default=date.today, null=True, blank=True)
    end_date = models.DateField('Дата завершения', default=date.today, null=True, blank=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'