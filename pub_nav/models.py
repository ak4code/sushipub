from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Menu(models.Model):
    POSITIONS = (
        (None, 'Выбрать позицию'),
        ('header', 'Шапка'),
        ('top-bar', 'Верхняя панель'),
        ('footer', 'Подвал'),
    )
    name = models.CharField(max_length=255, verbose_name='Название')
    position = models.CharField(max_length=20, blank=True, null=True, choices=POSITIONS, verbose_name='Позиция меню')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name='Меню')
    name = models.CharField(max_length=255, verbose_name='Название')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='childs', on_delete=models.CASCADE, verbose_name='Родитель')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True,)
    content_object = GenericForeignKey('content_type',  'object_id')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
