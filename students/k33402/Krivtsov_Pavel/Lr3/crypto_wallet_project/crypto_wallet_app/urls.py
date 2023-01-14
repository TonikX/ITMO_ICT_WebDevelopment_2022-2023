from django.urls import path
from . import views

urlpatterns = [
    path('currencies/', views.CurrenciesListApiView.as_view()),
    path('currencies/popular/', views.PopularCurrenciesListApiView.as_view()),
    path('currencies/<int:pk>/', views.CurrencyInfoApiView.as_view()),
    path('currencies/create/', views.CurrencyCreateApiView.as_view()),

    path('ownerships/all/', views.AllOwnershipListApiView.as_view()),
    path('ownerships/', views.UserOwnershipsListApiView.as_view()),
    path('ownership/create/', views.OwnershipCreateApiView.as_view()),
    path('ownership/change_count/<int:pk>/', views.OwnershipUpdateApiView.as_view()),

    path('transactions/all/', views.AllTransactionListApiView.as_view()),
    path('transactions/', views.UserTransactionsListApiView.as_view()),
    path('transaction/create/', views.TransactionCreateApiView.as_view()),

    path('discussions/', views.DiscussionsListApiView.as_view()),
    path('discussion/create/', views.DiscussionCreateApiView.as_view()),

    path('tags/', views.TagsListApiView.as_view()),
    path('tag/create/', views.TagCreateApiView.as_view()),

    path('comment/create/', views.CommentCreateApiView.as_view()),
    path('comments/<int:pk>', views.CommentsListApiView.as_view()),
]
