# settings.py
Sets up the work of service.

## INSTALLED_APPS:
* `'airport_app'` - Includes our app to project.
* `'rest_framework'` - Adds ability to use API.
* `'rest_framework.authtoken'` - Adds ability to use authentication.
* `'djoser'` - Adds Djoser.

## REST_FRAMEWORK:
* `'DEFAULT_AUTHENTICATION_CLASSES':`  Indicates authentication types that can be used.
    * `'rest_framework.authentication.TokenAuthentication'` - Adds token authentication.
    * `'rest_framework.authentication.BasicAuthentication'` - Adds authentication by login and password.
    * `'rest_framework.authentication.SessionAuthentication'` - Adds session authentication.