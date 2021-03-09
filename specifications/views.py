from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import NewCategoryForm, NewCategoryFeatureKeyForm, NewFeatureValueForm


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


class CreateNewFeatureValue(View):

    def get(self, request, *args, **kwargs):
        form = NewFeatureValueForm(request.POST or None)
        context = {'form': form}
        return render(request, 'specifications/new_feature_value.html', context)

    def post(self, request, *args, **kwargs):
        form = NewFeatureValueForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            new_feature_value = form.save(commit=False)
            new_feature_value.category = form.cleaned_data['category']
            new_feature_value.feature_key = form.cleaned_data['feature_key']
            new_feature_value.valid_feature_value = form.cleaned_data['valid_feature_value']
            new_feature_value.save()
            return HttpResponseRedirect('/product-specs/')
        return render(request, 'specifications/new_feature_value.html', context)
