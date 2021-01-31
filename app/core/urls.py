from django.urls import path

from . import views 
from core.views import UserProfilePageView, UserAccountSettingsView


urlpatterns = [
    path('elanlar/new/', views.NewProductFormView.as_view(), name='new-product-add-page'),
    path('', views.HomePageView.as_view(), name='home-page'),
    path('elanlar/new/', views.NewProductFormView.as_view(), name='new-product-add-page'),
    path('card/', views.BasicTestView.as_view()),
    path('profile/', UserProfilePageView.as_view(), name='user-profile'),
    path('profile-settings/', UserAccountSettingsView.as_view(), name='profile-settings'),
    path("product_detail/<slug>/", views.ProductView.as_view(),name="product-detail"),
]