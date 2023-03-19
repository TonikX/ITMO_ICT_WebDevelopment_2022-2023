В `laboratory_work_3_project/urls.py`:

``` python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('laboratory_work_3_app.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
```

В `laboratory_work_3_app/urls.py`:

``` python
book_instances_urlpatterns = [
    path('book_instances/all', BookInstancesListView.as_view()),
    path('book_instances/create', BookInstancesCreateView.as_view()),
    path('book_instances/<str:pk>', BookInstancesGetUpdateDeleteView.as_view())
]

books_urlpatterns = [
    path('books/all', BookListView.as_view()),
    path('books/create', BookCreateView.as_view()),
    path('books/<str:pk>', BooksGetUpdateDeleteView.as_view())
]

readers_urlpatterns = [
    path('readers/all', ReadersListView.as_view()),
    path('readers/all/with_books', ReadersWithBooksListView.as_view()),
    path('readers/create', ReadersCreateView.as_view()),
    path('readers/<str:pk>', ReadersGetUpdateDeleteView.as_view())
]

urlpatterns = (
    []
    + book_instances_urlpatterns
    + books_urlpatterns
    + readers_urlpatterns
)
```
