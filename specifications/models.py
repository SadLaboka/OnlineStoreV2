from django.db import models


class CategoryFeature(models.Model):
    """
    Характеристика конктретной категории
    """
    category = models.ForeignKey('main.Category', verbose_name='Категория', on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100, verbose_name='Имя характеристики')
    feature_filter_name = models.CharField(max_length=50, verbose_name='Имя фильтра')
    unit = models.CharField(max_length=50, verbose_name='Единица измерения', null=True, blank=True)

    def __str__(self):
        return f'{self.category.title} | {self.feature_name}'

    class Meta:
        unique_together = ('category', 'feature_name', 'feature_filter_name')


class FeatureValidator(models.Model):
    """
    Валидатор значений для конкретной характеристики, принадлежащей к конкретной категории
    """
    category = models.ForeignKey('main.Category', verbose_name='Категория', on_delete=models.CASCADE)
    feature_key = models.ForeignKey(CategoryFeature, verbose_name='Ключ характеристики', on_delete=models.CASCADE)
    valid_feature_value = models.CharField(max_length=100, verbose_name='Валидное значение')

    def __str__(self):
        return f'Категория "{self.category.title}" | Характеристика "{self.feature_key.feature_name}" | ' \
               f'Валидное значение "{self.valid_feature_value}"'


class ProductFeatures(models.Model):
    """
    Характеристики товара
    """
    product = models.ForeignKey('main.Product', verbose_name='Товар', on_delete=models.CASCADE)
    feature = models.ForeignKey(CategoryFeature, verbose_name='Характеристика', on_delete=models.CASCADE)
    value = models.CharField(max_length=255, verbose_name='Значение')

    def __str__(self):
        return f'Товар - "{self.product.title}" | Характеристика - "{self.feature.feature_name}"' \
               f'Значение - {self.value}'
