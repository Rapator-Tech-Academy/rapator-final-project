from django.urls import path

from . import views

app_name ='api'

urlpatterns = [
    path('get-products/', views.FilterProductListAPIView.as_view(), name="get-products"),
    path('user-products/<str:user_id>/', views.UserProductsListAPIView.as_view(), name='user-products'),
    path('user-info/<pk>/', views.UserInformationsListAPIView.as_view(), name='user-informations-update'),
]