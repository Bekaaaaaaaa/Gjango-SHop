
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderItemSerilizer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderItemSerilizer
    permission_classes = [IsAuthenticated]

