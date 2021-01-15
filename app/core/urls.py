from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('elanlar/new/', views.NewProductFormView.as_view(), name='new-product-add-page'),
    path('card/', views.BasicTestView.as_view())
]