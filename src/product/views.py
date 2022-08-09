from .models import Product, Category, Order, Consultation
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    OrderListSerializer,
    OrderCreateSerializer,
    ConsultationSerializer,
)
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from django.db.models import F


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("category_id",)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = "id"


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = "id"


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.select_related("product").annotate(
            size=F("product__size"),
            width=F("product__width"),
        )


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def perform_update(self, serializer):
        serializer.save()
        status = serializer.validated_data["status"]
        if status:
            pk = serializer.data["product"]
            product = Product.objects.get(id=pk)
            product.quantity -= serializer.data["quantity"]
            product.save()


class ConsultationListView(generics.ListAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = (IsAuthenticated,)


class ConsultationCreateView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


class ConsultationUpdateView(generics.UpdateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    lookup_field = "id"
    permission_classes = (IsAuthenticated,)
