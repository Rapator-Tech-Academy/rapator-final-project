from django.urls import path

from . import views

urlpatterns = [
    path('get-products/', views.FilterProductListAPIView.as_view(), name="get-products")
]