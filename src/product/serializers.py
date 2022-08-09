from rest_framework import serializers
from .models import Product, Category, Order, Consultation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    size = serializers.CharField()
    width = serializers.IntegerField()

    class Meta:
        model = Order
        fields = (
            "id",
            "name",
            "phone_number",
            "address",
            "status",
            "image",
            "size",
            "width",
            "date",
        )

    def get_image(self, obj):
        request = self.context.get("request")
        image_url = obj.product.image.url
        return request.build_absolute_uri(image_url)


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "name",
            "phone_number",
            "address",
            "product",
            "date",
            "status",
            "quantity",
        )


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ("name", "phone_number", "date", "status")
