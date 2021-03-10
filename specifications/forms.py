from django import forms

from shop.models import Category
from .models import CategoryFeature, ProductFeatures


class NewCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class NewCategoryFeatureKeyForm(forms.ModelForm):

    class Meta:
        model = CategoryFeature
        fields = '__all__'


class FeatureToProductForm(forms.ModelForm):

    class Meta:
        model = ProductFeatures
        fields = '__all__'


