from rest_framework import generics
from rest_framework.response import Response

from ..models import Category, Product, Rate
from .serializers import CategorySerializer, ProductSerializer, RateSerializer


class CategoryListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/product/category/list/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/account/product/list/
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        if q:
            qs = qs.filter(name__icontains=q)
        if cat:
            qs = qs.filter(category__title__iexact=cat)
        return qs


class RateCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/product/product-rate/
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class UpdateViewsAPIView(generics.RetrieveAPIView):
    # http://127.0.0.1:8000/product/product/views/{pk}
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

