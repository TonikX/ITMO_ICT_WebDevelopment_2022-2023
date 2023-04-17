# urls.py
Installs dependencies of urls in service.

## urlpatterns:
* `path('admin/', admin.site.urls)` - Allows access to admin panel.
* `path('', include('airport_app.url'))` - Includes urls from airport_app.
* `path('auth/', include('djoser.urls'))` - Adds authentication by `auth/` by Djoser.
* `re_path(r'^auth/', include('djoser.urls.authtoken'))` - Adds token authentication by Djoser.

