from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from datetime import datetime

class Mother(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Изоброжение профиля')
    first_name = models.CharField(verbose_name='Имя', max_length=124, null=False)
    last_name = models.CharField(verbose_name='Фамилия', max_length=124, null=False)
    weight = models.IntegerField(verbose_name='Вес')
    height = models.IntegerField(verbose_name='Рост')
    gestation_date = models.DateField(verbose_name='Дата беременности', null=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    city = models.CharField(verbose_name='Город', null=False, max_length=124)
    children_count = models.IntegerField(verbose_name='Количество детей', default=0, null=False)
    birth_date = models.DateField(verbose_name='Возраст', null=True)
    

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'


class Post(models.Model):
    author = models.ManyToManyField(Mother, verbose_name='Автор')
    photo = models.ImageField(verbose_name='Фото', null=True)
    title = models.CharField(verbose_name='Заголовок', null=False, max_length=254)
    description = models.TextField(verbose_name='Описание', null=False)

    def __str__(self) -> str:
        return self.title


# class Message(models.Model):
#     author = models.ManyToOneRel(Mother, on_delete=models.CASCADE)
#     from_to = models.ManyToOneRel(Mother, on_delete=models.CASCADE)
#     text = models.TextField(verbose_name='Текст', null=False)
#     date_send = models.DateTimeField(verbose_name='Дата отправки', default=datetime.now(), null=False)

#     def __str__(self):
#         return self.author