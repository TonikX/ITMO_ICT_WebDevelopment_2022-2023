"""Stream URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include("backend.app.urls")),
    path('profile/', include("backend.profiles.urls")),
    path('api/v1/app/', include('backend.api.app.urls')),
    path('api/v1/profile/', include('backend.api.profiles.urls')),
    path('api/v1/exhibition/', include('backend.api.exhibition.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
