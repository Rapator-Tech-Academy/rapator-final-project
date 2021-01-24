from django.urls import path

from . import views 


urlpatterns = [
    path('elanlar/new/', views.NewProductFormView.as_view(), name='new-product-add-page'),
    path('post/<slug>', views.PostView.as_view(), name="post"),
    path('', views.HomePageView.as_view(), name='home-page'),
    path('elanlar/new/', views.NewProductFormView.as_view(), name='new-product-add-page'),
    path('card/', views.BasicTestView.as_view()),
    path("product_detail", views.CategoryView.as_view(), name="home-page"),
]