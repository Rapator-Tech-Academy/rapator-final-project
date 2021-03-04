from django.urls import path

from . import views 

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('elanlar/new/', views.NewProductFormView.as_view(), name='new-product-add-page'),
    path('elanlar/', views.SearchResultPageView.as_view(), name='search-result-page'),
    path('elanlar/<slug>/', views.ProductView.as_view(),name='product-detail'),
    path('elanlar/<slug>/delete/', views.delete_product, name='delete-product'),
    path('elanlar/<slug>/ad_edits/', views.EditProductView.as_view(), name='product-edit-page'),
    path('profile/<str:condition>/', views.UserProfilePageView.as_view(), name='user-profile'),
    path('profile-settings/', views.UserAccountUpdateFormView.as_view(), name='profile-settings'),
]
