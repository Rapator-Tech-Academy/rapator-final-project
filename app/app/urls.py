from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import i18n

from rest_framework_simplejwt import views as jwt_views

urlpatterns = i18n.i18n_patterns(
    path('', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include("users.urls")),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
  
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),      

    path('api/', include('api.urls')),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
)

if 'rosetta' in settings.THIRD_PARTY_APPS:
    urlpatterns += (
        path('rosetta', include('rosetta.urls')),
    )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
