from django.db import models


class CategoryFeature(models.Model):
    """
    Характеристика конктретной категории
    """
    category = models.ForeignKey('shop.Category', verbose_name='Категория', on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100, verbose_name='Имя характеристики')
    feature_filter_name = models.CharField(max_length=50, verbose_name='Имя фильтра')
    unit = models.CharField(max_length=50, verbose_name='Единица измерения', null=True, blank=True)

    def __str__(self):
        return f'{self.category.title} | {self.feature_name}'

    class Meta:
        unique_together = ('category', 'feature_name', 'feature_filter_name')


class ProductFeatures(models.Model):
    """
    Характеристики товара
    """
    product = models.ForeignKey('shop.Product', verbose_name='Товар', on_delete=models.CASCADE)
    feature = models.ForeignKey(CategoryFeature, verbose_name='Характеристика', on_delete=models.CASCADE)
    value = models.CharField(verbose_name='Значение', max_length=100)

    def __str__(self):
        return f'Товар - "{self.product.title}" | Характеристика - "{self.feature.feature_name}"' \
               f'Значение - {self.value}'
