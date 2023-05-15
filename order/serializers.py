from rest_framework.serializers import ModelSerializer
from drf_writable_nested import WritableNestedModelSerializer

from .models import Order, OrderItem



class OrderItemSerilizer(ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ("order",)


class OrderSerializer(WritableNestedModelSerializer, ModelSerializer):
    items = OrderItemSerilizer(many=True)

    class Meta:
        models = Order
        fields = ("user", "is_paid", "created_at", "total_price", "items")
        