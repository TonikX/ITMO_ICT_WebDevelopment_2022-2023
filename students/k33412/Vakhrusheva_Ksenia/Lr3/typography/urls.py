from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
	openapi.Info(
		title="API",
		default_version='v3.0.3',
		description="Проект",
	),
	public=True,
)

urlpatterns = [
	path("", include("typography.views.author_view")),
	path("", include("typography.views.books_view")),
	path("", include("typography.views.customers_view")),
	path("", include("typography.views.editors_view")),
	path("", include("typography.views.managers_view")),
	path("", include("typography.views.orders_view")),
	path("", include("typography.views.profiles_view")),
	path("debug/", include("typography.views.fill-view")),

	# --

	path("auth/", include("djoser.urls")),
	re_path("^auth/", include("djoser.urls.authtoken")),
	path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
