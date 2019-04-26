from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from tinymce import HTMLField
from uuslug import uuslug


class AbstractShop(models.Model):
    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Мета заголовок')
    meta_description = models.TextField(blank=True, null=True, verbose_name='Мета описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


class Category(AbstractShop):
    name = models.CharField(max_length=255, verbose_name='Название')
    content = HTMLField(blank=True, null=True, verbose_name='Контент')
    image = models.ImageField(upload_to='shop/categories', blank=True, null=True, verbose_name='Изображение')
    slug = models.SlugField(blank=True, null=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.name, instance=self)
        super(Category, self).save(*args, **kwargs)

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
    image = models.ImageField(upload_to='shop/products', blank=True, null=True, verbose_name='Изображение')
    slug = models.SlugField(blank=True, null=True, verbose_name='Ссылка')
    ingredients = models.ManyToManyField('Ingredient', blank=True, verbose_name='Ингредиенты')
    quantity = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество шт.')
    weight = models.PositiveIntegerField(blank=True, null=True, verbose_name='Вес в гр.')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.name, instance=self)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'category_slug': self.category.slug, 'product_slug': self.slug})

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
        else:
            return mark_safe('<img src="/static/src/assets/img/noimage.png" width="50" height="50" />')

    image_tag.short_description = 'Просмотр изображения'

    class Meta:
        ordering = ['pk']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
