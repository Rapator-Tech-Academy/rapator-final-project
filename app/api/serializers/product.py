from django.contrib.auth import get_user_model

from rest_framework import serializers

from core.models import Product

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'price', 'slug', 'description', 'image_url', 'city', 'status']
    
    def get_image_url(self, obj):
        return obj.get_image_url()
    
    def get_city(self, obj):
        return obj.city.name