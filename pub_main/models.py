from django.db import models
from solo.models import SingletonModel
from tinymce import HTMLField


class Shop(SingletonModel):
    name = models.CharField(max_length=60, default='Магазин', verbose_name='Название')
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')
    meta_description = models.TextField(blank=True, null=True, verbose_name='Мета описание')

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
    name = models.CharField(max_length=20, verbose_name='Название')
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

    class Meta:
        verbose_name_plural = 'Страница'
        verbose_name = 'Страницы'
