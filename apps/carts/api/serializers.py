from rest_framework import serializers
from ..models import Cart, CartItem, WishList, Order
from ...accounts.serializers import AccountSerializer
from ...products.api.serializers import ProductSerializer


class WishlistSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    product = ProductSerializer()

    class Meta:
        model = WishList
        fields = ['id', 'user', 'product']


class WishlistCreateSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = WishList
        fields = ['id', 'user', 'product', 'user_email']
        extra_kwargs = {
            'user': {'required': False}
        }


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total']


class CartSerializer(serializers.ModelSerializer):
    client = AccountSerializer(read_only=True)
    cart_items = CartItemSerializer()

    def get_cart_items(self, obj):
        qs = CartItem.objects.filter(cart_id=obj.id)
        sz = CartItemSerializer(qs, many=True)
        return sz.data

    class Meta:
        model = Cart
        fields = ['id', 'client', 'is_ordered', 'cart_items', 'get_cart_items', 'get_cart_total']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['cart', 'client', 'phone', 'address', 'transaction_id', 'note', 'status']
        extra_kwargs = {
            'transaction_id': {'read_only': True},
            'client': {'required': False},
            'cart': {'required': False},

        }
