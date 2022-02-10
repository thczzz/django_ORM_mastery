from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from polymorphic.models import PolymorphicModel


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


####################################
"""  Polymorphic Inheritance  """
####################################

"""
class Product(PolymorphicModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    ##### 6 queries in 2.00 ms with Product.objects.all(), check the view + template
"""


####################################
"""  Abstract Model Inheritance  """
####################################

"""""
class Product(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('book', 'cupboard')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class Base(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created',)


class Book(Base):
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    m2m = models.ManyToManyField(Product, related_name="store_book_related", related_query_name="book")


class Cupboard(Base):
    shelves = models.IntegerField()
    author = models.CharField(max_length=255)
    m2m = models.ManyToManyField(Product, related_name="store_cupboard_related", related_query_name="cupboard")


    ### 8 queries in 2.00 ms with Product.objects.all().select_related('content_type')
"""""


####################################
"""  Multi-table Inheritance  """
####################################


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    ### 12 queries in 4.00 ms with Product.objects.all()
    ### 6 queries in 2.00 ms with Product.objects.all().prefetch_related('book', 'cupboard')
    ### 4 queries in 1.00 ms with Product.objects.all().select_related('book', 'cupboard')


class Book(Product):
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)


class Cupboard(Product):
    shelves = models.IntegerField()
    author = models.CharField(max_length=255)
