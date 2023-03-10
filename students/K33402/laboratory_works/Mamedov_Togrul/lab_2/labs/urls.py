from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('work_space.urls', namespace='work')),
    path('auth/', include('users.urls', namespace='auth')),
]
