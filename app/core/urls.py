from django.urls import path
from . import views



urlpatterns = [
    path('elanlar/new/', views.NewProductFormView.as_view(), name='new-product-add-page'),
    path('home/', views.HomePageView.as_view(), name="homepage"), #added
    path('card/', views.BasicTestView.as_view()),
    path('profile/', views.UserProfilePageView.as_view(), name='user-profile'),
    path('post/<slug>', views.PostView.as_view(), name="post"),
    path('profile-settings/', views.UserAccountSettingsView.as_view(), name='profile-settings'),
    path("product_detail", views.CategoryView.as_view(), name="product-detail"),
]

