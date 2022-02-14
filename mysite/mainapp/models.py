from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64,
                            unique=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование', max_length=64)
    description = models.TextField(verbose_name='Описание товара',
                                   blank=True)
    short_desc = models.CharField(verbose_name='Краткое описание',
                                  max_length=64, blank=True)
    image = models.ImageField(verbose_name='Изображение',
                              upload_to='products_images', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8,
                                decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во на складе',
                                           default=0)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name}"
