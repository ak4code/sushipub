from django.db import models
from django.urls import reverse
from tinymce import HTMLField


class AbstractShop(models.Model):
    meta_description = models.TextField(blank=True, null=True, verbose_name='Мета описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


class Category(AbstractShop):
    name = models.CharField(max_length=255, verbose_name='Название')
    content = HTMLField(blank=True, null=True, verbose_name='Контент')
    image = models.ImageField(upload_to='shop/categories', blank=True, null=True, verbose_name='Изображение')
    slug = models.SlugField(default='slug', verbose_name='Ссылка')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.slug)])

    class Meta:
        ordering = ['pk']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(AbstractShop):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория', on_delete=models.CASCADE)
    content = HTMLField(blank=True, null=True, verbose_name='Контент')
    price = models.DecimalField(max_digits=10, default=0, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='shop/categories', blank=True, null=True, verbose_name='Изображение')
    slug = models.SlugField(default='slug', verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
