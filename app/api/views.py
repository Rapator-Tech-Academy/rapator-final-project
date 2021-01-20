from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from core.models import Product
from .serializers import *

User = get_user_model()

# Create your views here.

class FilterProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        query = Product.objects.filter(status=1)
        data = self.request.query_params

        if data.get('max'):
            kw = data.get('max')
            query = query.filter(price__lte=kw)
        
        if data.get('min'):
            kw = data.get('min')
            query = query.filter(price__gte=kw)

        return query


class UserProductsListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']

        if user_id:
            query = Product.objects.filter(user__id=user_id)

            return query


class UserInformationsListAPIView(RetrieveUpdateAPIView):
    serializer_class = UserInformationSerializer
    queryset = User.objects.all()
    
    def get_queryset(self):
        user_id = self.kwargs['pk']

        if user_id:
            queryset = User.objects.filter(id=user_id)

            return queryset