from django.urls import path

from .views import temp_main, ProductDetailView, CategoryDetailView

urlpatterns = [
    path('', temp_main, name='home'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]
