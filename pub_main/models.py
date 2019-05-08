from django.db import models
from django.urls import reverse
from solo.models import SingletonModel
from tinymce import HTMLField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Shop(SingletonModel):
    name = models.CharField(max_length=60, default='Магазин', verbose_name='Название')
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')
    work = models.CharField(max_length=60, default='Заказ с 11:00 до 24:00', verbose_name='Режим работы')
    meta_title = models.CharField(max_length=150, blank=True, null=True, verbose_name='Мета заголовок')
    meta_description = models.TextField(blank=True, null=True, verbose_name='Мета описание')
    content = HTMLField(blank=True, null=True, verbose_name='Контент')

    def get_primary_phone(self):
        return self.phones.get(primary=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'


class Phone(models.Model):
    number = models.CharField(max_length=20, verbose_name='Телефон')
    primary = models.BooleanField(default=False, verbose_name='Основной')
    shop = models.ForeignKey('Shop', related_name='phones', on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class Link(models.Model):
    LINK_TYPE = (
        ('instagram', 'Instagram'),
        ('vk', 'ВКонтакте'),
        ('ok', 'Одноклассники'),
        ('web', 'Другое'),
    )
    name = models.CharField(max_length=20, choices=LINK_TYPE, default='web', verbose_name='Название')
    url = models.CharField(max_length=255, verbose_name='Ссылка')
    shop = models.ForeignKey('Shop', related_name='links', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'


class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = HTMLField(blank=True, null=True, verbose_name='Контент')
    meta_title = models.CharField(max_length=150, blank=True, null=True, verbose_name='Мета заголовок')
    meta_description = models.TextField(blank=True, null=True, verbose_name='Мета описание')
    slug = models.SlugField(verbose_name='Ссылка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', args=[str(self.slug)])

    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    position = models.CharField(max_length=20, default=None, unique=True, db_index=True,
                                verbose_name='Позиция меню')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name='Меню')
    name = models.CharField(max_length=255, verbose_name='Название')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='childs', on_delete=models.CASCADE,
                               verbose_name='Родитель')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True, )
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
