from django import forms

from shop.models import Category
from .models import CategoryFeature, FeatureValidator


class NewCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class NewCategoryFeatureKeyForm(forms.ModelForm):

    class Meta:
        model = CategoryFeature
        fields = '__all__'


class NewFeatureValueForm(forms.ModelForm):

    class Meta:
        model = FeatureValidator
        fields = '__all__'
