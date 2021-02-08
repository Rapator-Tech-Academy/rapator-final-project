from datetime import date

from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.models import Product
from .serializers import *

User = get_user_model()

# Create your views here.

class FilterProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        query = Product.objects.filter(status=1).order_by('-updated_at')

        data = self.request.query_params

        if data.get('keyword'):
            kw = data.get('keyword')
            query = query.filter(title__icontains=kw)

        if data.get('max'):
            kw = data.get('max')
            query = query.filter(price__lte=kw)
        
        if data.get('min'):
            kw = data.get('min')
            query = query.filter(price__gte=kw)
            
        return query


class UserProductsListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']

        if user_id:
            query = Product.objects.filter(user__id=user_id)

            return query


class UserInformationsListAPIView(RetrieveUpdateAPIView):
    serializer_class = UserInformationSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user_id = self.kwargs['pk']

        if user_id:
            queryset = User.objects.filter(id=user_id)

            return queryset
    

class AuthView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class StatisticsView(APIView):
    date_of_today = date.today()

    def daily_registered_new_user(self):
        user_count = User.objects.filter(date_joined__gt=self.date_of_today).count()

        return str(user_count)

    def daily_product_view_count(self):
        daily_view_count = 0

        for product in Product.objects.all():
            daily_view_count += product.daily_view_count

        return str(daily_view_count)
    
    def daily_added_new_product_count(self):
        
        product_count = Product.objects.filter(created_at__gt=self.date_of_today, status=1).count()

        return str(product_count)

    def get(self, request):
        
        context = {
            'daily_new_user': self.daily_registered_new_user(),
            'daily_product_views': self.daily_product_view_count(),
            'daily_added_new_products': self.daily_added_new_product_count(),
        }

        return Response(context)