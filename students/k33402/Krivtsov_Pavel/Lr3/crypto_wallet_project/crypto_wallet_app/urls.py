from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('currencies/', views.CurrenciesListApiView.as_view()),
    path('currencies/popular/', views.PopularCurrenciesListApiView.as_view()),
    path('currencies/<int:pk>/', views.CurrencyInfoApiView.as_view()),
    path('currencies/create/', views.CurrencyCreateApiView.as_view()),

    path('ownerships/all/', views.AllOwnershipListApiView.as_view()),
    path('ownerships/', views.UserOwnershipsListApiView.as_view()),
    path('ownerships/create/', views.OwnershipCreateApiView.as_view()),
    path('ownerships/change_count/<int:pk>/', views.OwnershipUpdateApiView.as_view()),

    path('transactions/all/', views.AllTransactionListApiView.as_view()),
    path('transactions/', views.UserTransactionsListApiView.as_view()),
    path('transactions/create/', views.TransactionCreateApiView.as_view()),

    path('discussions/', views.DiscussionsListApiView.as_view()),
    path('discussions/create/', views.DiscussionCreateApiView.as_view()),

    path('tags/', views.TagsListApiView.as_view()),
    path('tags/create/', views.TagCreateApiView.as_view()),

    path('comments/create/', views.CommentCreateApiView.as_view()),
    path('comments/<int:pk>', views.CommentsListApiView.as_view()),
]
