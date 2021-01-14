from django.urls import path

from . import views


urlpatterns = [
    path('elanlar/new/', views.NewProductFormView.as_view(), name='new-product-add-page')
    
]