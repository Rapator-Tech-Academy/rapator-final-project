from django.contrib.auth import get_user_model

from rest_framework import serializers

from core.models import Product

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    date_time = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'price', 'slug', 'description', 'image_url', 'city', 'status', 'date', 'date_time']
    
    def get_image_url(self, obj):
        if obj.image:
            return obj.get_image_url()
        return 'null'
    
    def get_city(self, obj):
        return obj.city.name
    
    def get_date(self, obj):
        date = obj.is_past_due
        return date
    
    def get_date_time(self, obj):
        date_time = obj.updated_at.strftime("%H:%M")
        return date_time
    
