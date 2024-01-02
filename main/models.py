from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(verbose_name='Category name', max_length=50, db_index=True)
    slug = models.SlugField(verbose_name='Identificator', unique=True)
    description = models.CharField(verbose_name='Short Description', max_length=255)
    text = RichTextField(verbose_name='Long Description')
    image = ResizedImageField(default='category_pics/default.png', verbose_name='Image', upload_to='category_pics/', size=[500, 500])
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    title = models.CharField(verbose_name='Product name', max_length=50)
    description = models.TextField(verbose_name='Short Description', max_length=255)
    text = RichTextField(verbose_name='Long Description')
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Price')
    total = models.IntegerField(verbose_name='Total')
    image = ResizedImageField(default='product_pics/default.png', verbose_name='Image', upload_to='product_pics/', size=[540, 360])
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    is_active = models.BooleanField(default=True, verbose_name='Status')
    slug = models.SlugField(verbose_name='Identificator', unique=True)
    color = models.CharField(verbose_name='Color', blank=True, null=True, max_length=55)
    material = models.CharField(verbose_name='Material', blank=True, null=True, max_length=55)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'


class ProductCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=0)


class AboutPage(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.TextField(max_length=600, verbose_name='Short description')
    text = RichTextField(verbose_name='Content of detail page')
    changed_at = models.DateTimeField(auto_now=True)
    image = ResizedImageField(verbose_name='Image', default='page_pics/default.png', upload_to='page_pics/', size=[540, 419])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '"About Page"'
        verbose_name_plural = '"About Pages"'


class ProductComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Content', max_length=5000)
    sent_at = models.DateTimeField(auto_now_add=True)




