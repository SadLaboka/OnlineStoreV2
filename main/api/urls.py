from django.urls import path

from .api_views import (
    CategoryListAPIView,
    SmartphoneListAPIView,
    NotebookListAPIView,
    SmartphoneDetailAPIView,
    NotebookDetailAPIView,
    CustomersListAPIView,
)


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('notebooks/', NotebookListAPIView.as_view(), name='notebooks'),
    path('notebooks/<str:slug>/', NotebookDetailAPIView.as_view(), name='notebook_detail'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones'),
    path('smartphones/<str:slug>/', SmartphoneDetailAPIView.as_view(), name='smartphone_detail'),
    path('customers/', CustomersListAPIView.as_view(), name='customers'),
]
