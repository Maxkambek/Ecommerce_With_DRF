from django.http import JsonResponse
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from .serializers import WishlistSerializer, WishlistCreateSerializer, CartSerializer, CartItemSerializer, \
    OrderSerializer
from ..models import WishList, Cart, Order, CartItem
from ...products.models import Product


class WishlistListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/cart/wishlist/list-create/
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return super().get_queryset().filter(user_id=user_id)

    def create(self, request, *args, **kwargs):
        serializer = WishlistCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user_id = self.request.user.id
        serializer.save(user_id=user_id)


class MyCartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset().filter(client=self.request.user, is_ordered=False)
        return qs


class DeleteFromMyCart(generics.RetrieveDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddToMyCartAPIView(views.APIView):
    queryset = Cart.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pid = request.data.get('_pid')
        user = request.user
        product = Product.objects.filter(id=pid)
        my_cart, new_cart = Cart.objects.get_or_create(client=user, is_ordered=False)
        data = None
        if my_cart:
            CartItem.objects.create(product=product, cart=my_cart)
            data = {
                'success': True,
                'product': product.name
            }
        if new_cart:
            CartItem.objects.create(product=product, cart=new_cart)
            data = {
                'success': True,
                'product': product.name
            }
        return JsonResponse(data, status=201)


class OrderAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/cart/order/
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        cart_id = request.data.get('cart_id')
        serializer.is_valid(raise_exception=True)
        serializer.save(client_id=request.user.id, cart_id=cart_id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
