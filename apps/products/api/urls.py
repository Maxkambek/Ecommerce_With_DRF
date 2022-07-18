from django.urls import path
from . import views

urlpatterns = [
    path('category/list/', views.CategoryListAPIView.as_view()),
    path('product/list/', views.ProductListAPIView.as_view()),
    path('product-rate/', views.RateCreateAPIView.as_view()),
    path('product/view/<int:pk>/', views.UpdateViewsAPIView.as_view()),
]
