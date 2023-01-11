from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from typography.views.author_view import AuthorsApiView, GetAndPatchAuthorApiView, get_author_full
from typography.views.books_view import BooksApiView, GetAndPatchBookApiView, get_book_full
from typography.views.customers_view import CustomersApiView, get_customer_full, get_customer_full_me
from typography.views.editors_view import EditorsApiView, GetEditorApiView, get_editor_full
from typography.views.fill_view import fill_data
from typography.views.managers_view import ManagersApiView, GetManagerApiView
from typography.views.orders_view import OrdersApiView, OrderSingleViewDeleteAPIView
from typography.views.profiles_view import get_profiles

schema_view = get_schema_view(
	openapi.Info(
		title="API",
		default_version='v3.0.3',
		description="Проект",
	),
	public=True,
)

urlpatterns = [
	path("authors/", AuthorsApiView.as_view()),
	path("author/<int:pk>", GetAndPatchAuthorApiView.as_view()),
	path("author/<int:pk>/full", get_author_full),

	path("books/", BooksApiView.as_view()),
	path("book/<int:pk>", GetAndPatchBookApiView.as_view()),
	path("book/<int:pk>/full", get_book_full),

	path("customers/", CustomersApiView.as_view()),
	path("customer/<int:pk>", get_customer_full),
	path("customer/me", get_customer_full_me),

	path("editors/", EditorsApiView.as_view()),
	path("editor/<int:pk>", GetEditorApiView.as_view()),
	path("editor/<int:pk>/full", get_editor_full),

	path("managers/", ManagersApiView.as_view()),
	path("manager/<int:pk>", GetManagerApiView.as_view()),

	path("orders/", OrdersApiView.as_view()),
	path("order/<int:pk>", OrderSingleViewDeleteAPIView.as_view()),

	path("profiles/", get_profiles),

	path("debug/fill/", fill_data),

	# --

	path("auth/", include("djoser.urls")),
	re_path("^auth/", include("djoser.urls.authtoken")),
	path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
