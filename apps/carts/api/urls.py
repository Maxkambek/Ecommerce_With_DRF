from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/list-create/', views.WishlistListCreateAPIView.as_view()),
    path('my-cart/', views.MyCartListAPIView.as_view()),
    path('add-to-cart/', views.AddToMyCartAPIView.as_view()),
    path('my-cart/<int:pk>/', views.DeleteFromMyCart.as_view()),
    path('order/', views.OrderAPIView.as_view()),

]
