from rest_framework.generics import ListAPIView

from core.models import Product
from .serializers import ProductSerializer

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

