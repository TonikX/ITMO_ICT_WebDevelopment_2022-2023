from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('signup/', views.SignUp.as_view(), name="sign_up"),
    path('login/', views.LogIn.as_view(), name="log_in"),
    path('logout/', views.LogOut.as_view(), name="log_out"),


    # Basic model API views
    path('users/', views.UsersAPIView.as_view(), name="users"),
    path('user/<int:pk>', views.UserDetailsAPIView.as_view(), name="user_details"),

    path('libraries/', views.LibrariesAPIView.as_view(), name="libraries"),
    path('library/<int:pk>', views.LibraryDetailsAPIView.as_view(),
         name="library_details"),

    path('reading-rooms/', views.ReadingRoomsAPIView.as_view(), name="reading_rooms"),
    path('reading-room/<int:pk>', views.ReadingRoomDetailsAPIView.as_view(),
         name="reading_room_details"),

    path('books/', views.BooksAPIView.as_view(), name="books"),
    path('book/<int:pk>', views.BookDetailsAPIView.as_view(), name="book_details"),

    path('reading-room-books/', views.ReadingRoomBooksAPIView.as_view(),
         name="reading_room_books"),
    path('reading-room-book/<int:pk>', views.ReadingRoomBookDetailsAPIView.as_view(),
         name="reading_room_book_details"),

    path('reading-room-book-users/', views.ReadingRoomBookUsersAPIView.as_view(),
         name="reading_room_book_users"),
    path('reading-room-book-user/<int:pk>', views.ReadingRoomBookUserDetailsAPIView.as_view(),
         name="reading_room_book_user_details"),


    # Custom API views
    path('user-books/<int:pk>',
         views.UserBooksAPIView.as_view(), name="user_books"),
    path('users-books-overdue/',
         views.UsersYoungAPIView.as_view(), name="users_books_overdue"),
    path('users-books-rare/',
         views.UsersBooksRareAPIView.as_view(), name="users_books_rare"),
    path('users-young/',
         views.UsersYoungAPIView.as_view(), name="users_young"),
    path('users-degree/',
         views.UsersGroupedByDegreeAPIView.as_view(), name="users_degree"),
    path('library-monthly-report/<int:pk>',
         views.LibraryMonthlyReportAPIView.as_view(), name="library_monthly_report"),



    # path('profile/', views.Profile.as_view(), name="profile"),
    # path('flights/', views.Flights.as_view(), name="flights"),
    # path('flight/<int:pk>', views.FlightDetails.as_view(), name="flight_details"),
    # path('flight/reserve/<int:pk>', views.toggle_reserve, name="toggle_reserve"),
    # path('flight/passengers/<int:pk>',
    #      views.FlightPassengers.as_view(), name="flight_passengers"),
    # path('flight/reviews/<int:pk>',
    #      views.FlightReviews.as_view(), name="flight_reviews"),
    # path('flight/review/create/<int:pk>',
    #      views.FlightReviewCreate.as_view(), name="flight_review_create"),
]
