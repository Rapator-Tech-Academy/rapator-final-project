from django.urls import path

from . import views 
from core.views import UserProfilePageView, UserAccountUpdateFormView


urlpatterns = [
    path('elanlar/new/', views.NewProductFormView.as_view(), name='new-product-add-page'),
    path('', views.HomePageView.as_view(), name='home-page'),
    path('card/', views.BasicTestView.as_view()),
    path('profile/', UserProfilePageView.as_view(), name='user-profile'),
    path('profile-settings/', UserAccountSettingsView.as_view(), name='profile-settings'),
    path("elanlar/<slug>/", views.ProductView.as_view(),name="product-detail"),
    path("user_product_detail/<slug>/", views.ProductDetailView.as_view(),name="product-detail"),
    path('elanlar/<slug>/ad_edits', views.EditProductView.as_view(), name='product-edit-page'),
    path('elanlar/', views.SearchResultPageView.as_view(), name='search-result-page'),
    path('test/', views.BasicTestView.as_view(), name='test')
]
