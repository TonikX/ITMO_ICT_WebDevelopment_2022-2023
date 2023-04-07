from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# Список URL для администрирования, отображения
# других страниц 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html")),
    path("", include("flights.urls")),
    path("", include("authentication.urls"))
]
