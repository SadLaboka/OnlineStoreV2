from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import NewCategoryForm, NewCategoryFeatureKeyForm, FeatureToProductForm


class BaseSpecView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'specifications/product_features.html', {})


class NewCategoryView(View):

    def get(self, request, *args, **kwargs):
        form = NewCategoryForm(request.POST or None)
        context = {'form': form}
        return render(request, 'specifications/new_category.html', context)

    def post(self, request, *args, **kwargs):
        form = NewCategoryForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product-specs/')
        return render(request, 'specifications/new_category.html', context)


class CreateNewFeature(View):

    def get(self, request, *args, **kwargs):
        form = NewCategoryFeatureKeyForm(request.POST or None)
        context = {'form': form}
        return render(request, 'specifications/new_feature.html', context)

    def post(self, request, *args, **kwargs):
        form = NewCategoryFeatureKeyForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            new_category_feature_key = form.save(commit=False)
            new_category_feature_key.category = form.cleaned_data['category']
            new_category_feature_key.feature_name = form.cleaned_data['feature_name']
            new_category_feature_key.save()
            return HttpResponseRedirect('/product-specs/')
        return render(request, 'specifications/new_feature.html', context)


class SetFeatureToProduct(View):

    def get(self, request, *args, **kwargs):
        form = FeatureToProductForm(request.POST or None)
        context = {'form': form}
        return render(request, 'specifications/set_feature.html', context)

    def post(self, request, *args, **kwargs):
        form = FeatureToProductForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            set_feature = form.save(commit=False)
            set_feature.product = form.cleaned_data['product']
            set_feature.feature = form.cleaned_data['feature']
            set_feature.value = form.cleaned_data['value']
            set_feature.save()
            return HttpResponseRedirect('/product-specs/')
        return render(request, 'specifications/set_feature.html', context)
