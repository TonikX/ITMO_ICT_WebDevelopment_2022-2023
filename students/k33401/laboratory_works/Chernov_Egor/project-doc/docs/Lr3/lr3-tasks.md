##  Structure of project

* **hotel** - settings of project, include the authentication
* **account_app** - user registration
* **hotel_app** - interface for hotels, room types and rooms
* **reg_com_app** - interface for registration and comment
* **API** - description of API documentation

## hotel
* `settings.py`

Add configurations:
```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'rest_framework_simplejwt',
    'djoser',
    'hotel_app',
    'account_app',
    'reg_com_app',
]

MIDDLEWARE = [
    ...,
    'corsheaders.middleware.CorsMiddleware',
]
```
Change configurations for database:
```python
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "drf_hotel",
        "USER": "postgres",
        "PASSWORD": "Rabotadb123",
        "HOST": "localhost",
        "PORT": "5433",
    }
}
```
Add configurations for rest framework:
```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```
Add configurations for jwt:
```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

CORS_ALLOW_ALL_ORIGINS = True
```

* `urls.py`

Add configurations for documentation (swagger, redoc) and declare path for getting token and authentication:
```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Description:",
        terms_of_service="https://drive.google.com/file/d/1QxQo5jln6soFUj6EmOVEo1yauCo375PP/view",
        contact=openapi.Contact(email="krish19poroh@mail.ru"),
        license=openapi.License(name="API for the project \"Hotel\""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/', include('djoser.urls')),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('hotel_app.urls')),
]
```

## account_app
* `models.py`

Add models:
```python
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from hotel_app.models import Hotel


class Guest(models.Model):
    user_g = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_guest", verbose_name='ID User')
    phone_guest = models.CharField(max_length=10, verbose_name="Phone")
    passport_guest = models.CharField(max_length=10, null=True, blank=True, verbose_name="Passport")


class Employee(models.Model):
    user_empl = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_employee",
                                     verbose_name='ID User')
    hotel_empl = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name="hotel_employee", verbose_name='ID Hotel')
    phone_employee = models.CharField(max_length=10, verbose_name="Phone")
    position_employee = models.CharField(max_length=100, verbose_name="Position")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Guest.objects.create(user_g=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_staff:
        try:
            if Guest.objects.get(user_g=instance):
                Guest.objects.filter(user_g=instance).delete()
            Employee.objects.create(user_empl=instance)
        except:
            print('Employee already exist')
    else:
        try:
            if Employee.objects.all():
                if Employee.objects.get(user_empl=instance):
                    Employee.objects.filter(user_empl=instance).delete()
        except:
            print('No such employee')
```
* `permissions.py`

Create permission:
```python
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False
```
* `views.py`

Add views:
```python
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.models import User

from .serializers import MyUserSerializer
from .permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny, ]
        elif self.action in ('list', 'retrieve', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser | IsOwner, ]
        return [permission() for permission in self.permission_classes]
```
* `serializers.py`

Add serializers:
```python
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Guest, Employee


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('phone_guest', 'passport_guest')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('hotel_empl', 'phone_employee', 'position_employee')
        depth = 1


class MyUserSerializer(serializers.ModelSerializer):
    user_guest = GuestSerializer(required=False)
    user_employee = EmployeeSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'user_guest', 'user_employee')
```
* `urls.py`

Add urls:
```python
from django.urls import path

from .views import UserViewSet


urlpatterns = [
    path('user/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
```

## hotel_app
* `models.py`

Add models:
```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Hotel(models.Model):
    name_hotel = models.CharField(max_length=100, verbose_name='Name')
    city_hotel = models.CharField(max_length=100, verbose_name='City')
    address_hotel = models.CharField(max_length=255, verbose_name='Address')
    rating_hotel = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],
                                                    null=True,
                                                    blank=True,
                                                    verbose_name='Rating')
    des_hotel = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description')


class RoomType(models.Model):
    TYPE_CHOICES = [
        ("E", 'Econom'),
        ("S", 'Standard'),
        ("L", 'Lux'),
    ]

    hotel_rt = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_room_type",
                                 verbose_name='ID Hotel')
    type_rt = models.CharField(max_length=1, choices=TYPE_CHOICES, verbose_name='Type')
    rating_rt = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],
                                                 null=True,
                                                 blank=True,
                                                 verbose_name='Rating')
    price_rt = models.PositiveIntegerField(verbose_name='Price')
    des_rt = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description')


class Room(models.Model):
    STATUS_CHOICES = [
        ("F", 'Free'),
        ("T", 'Taken'),
        ("B", 'Booked'),
    ]

    hotel_r = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_room", verbose_name='ID Hotel')
    rt_r = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="rt_room", verbose_name='ID Room type')
    number_room = models.PositiveIntegerField(verbose_name='Number')
    status_room = models.CharField(max_length=1, choices=STATUS_CHOICES, default='F', verbose_name='Status')
    review_room = models.CharField(max_length=255, null=True, blank=True, verbose_name='Review')
```
* `views.py`

Add views:
```python
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Hotel, RoomType, Room
from .serializers import HotelSerializer, RoomTypeSerializer, RoomSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny, ]
        elif self.action in ('retrieve', 'create', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser, ]
        return [permission() for permission in self.permission_classes]


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny, ]
        elif self.action in ('retrieve', 'create', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser, ]
        return [permission() for permission in self.permission_classes]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny, ]
        elif self.action in ('retrieve', 'create', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser, ]
        return [permission() for permission in self.permission_classes]
```
* `serializers.py`

Add serializers:
```python
from rest_framework import serializers

from .models import Hotel, RoomType, Room


# Common
class CommonHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name_hotel')


class CommonRoomTypeSerializer(serializers.ModelSerializer):
    type_rt = serializers.CharField(source='get_type_rt_display')

    class Meta:
        model = RoomType
        fields = ('id', 'type_rt', 'rating_rt', 'price_rt', 'des_rt')


# Hotel
class HotelSerializer(serializers.ModelSerializer):
    hotel_room_type = CommonRoomTypeSerializer(many=True)

    class Meta:
        model = Hotel
        fields = '__all__'


# RoomType
class RoomTypeRoomSerializer(serializers.ModelSerializer):
    status_room = serializers.CharField(source='get_status_room_display')

    class Meta:
        model = Room
        fields = ('id', 'number_room', 'status_room', 'review_room')


class RoomTypeSerializer(serializers.ModelSerializer):
    hotel_rt = CommonHotelSerializer()
    rt_room = RoomTypeRoomSerializer(many=True)
    type_rt = serializers.CharField(source='get_type_rt_display')

    class Meta:
        model = RoomType
        fields = '__all__'


# Room
class RoomSerializer(serializers.ModelSerializer):
    hotel_r = CommonHotelSerializer()
    rt_r = CommonRoomTypeSerializer()
    status_room = serializers.CharField(source='get_status_room_display')

    class Meta:
        model = Room
        fields = '__all__'
```
* `urls.py`

Add urls:
```python
from django.urls import path, include

from .views import HotelViewSet, RoomTypeViewSet, RoomViewSet

urlpatterns = [
    path('account/', include('account_app.urls')),
    path('act/', include('reg_com_app.urls')),
    path('hotel/', HotelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('hotel/<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('hotel/room_type/<int:pk>/', RoomTypeViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('hotel/room_type/room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
]
```

## reg_com_app
* `models.py`

Add models:
```python
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from hotel_app.models import Hotel, RoomType, Room


class Registration(models.Model):
    STATUS_REG_CHOICES = [
        ('T', 'Taken'),
        ('B', 'Booked'),
    ]
    STATUS_PAY_CHOICES = [
        ('YP', 'Paid for'),
        ('NP', 'Not paid for'),
    ]

    user_reg = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='user_registration', verbose_name='ID User')
    hotel_reg = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='hotel_registration', verbose_name='ID Hotel')
    rt_reg = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='rt_registration', verbose_name='ID Room type')
    room_reg = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='room_registration', verbose_name='ID Room')

    employee_reg = models.PositiveIntegerField(null=True, blank=True, verbose_name='ID Employee')
    status_reg_reg = models.CharField(max_length=1, choices=STATUS_REG_CHOICES, verbose_name='Registration status')
    status_pay_reg = models.CharField(max_length=2, choices=STATUS_PAY_CHOICES, verbose_name='Payment status')
    check_in_reg = models.DateField(null=False, blank=False, verbose_name='Check in')
    check_out_reg = models.DateField(null=False, blank=False, verbose_name='Check out')
    booking_reg = models.DateField(null=False, blank=False, verbose_name='Booking date')


class Comment(models.Model):
    user_com = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_comment',
                                 verbose_name='ID Guest')
    room_com = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_comment', verbose_name='ID Room')

    rating_com = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                                  verbose_name='Rating')
    review_com = models.TextField(max_length=255, null=True, blank=True, verbose_name='Review')
    check_in_com = models.DateField(null=False, blank=False, verbose_name='Check in')
    check_out_com = models.DateField(null=False, blank=False, verbose_name='Check out')
```
* `permissions.py`

Create permissions:
```python
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False
```
* `views.py`

Add views:
```python
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Registration, Comment
from .serializers import RegistrationSerializer, CommentSerializer
from .permisions import IsOwner


class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAdminUser | IsOwner, ]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Registration.objects.all()
        return Registration.objects.filter(user_reg=user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny, ]
        elif self.action in ('create', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser | IsOwner, ]
        return [permission() for permission in self.permission_classes]
```
* `serializers.py`

Add serializers:
```python
from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Registration, Comment
from hotel_app.models import Hotel, RoomType, Room


# Common
class RegComUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class RegComHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name_hotel')


class RegComRoomTypeSerializer(serializers.ModelSerializer):
    type_rt = serializers.CharField(source='get_type_rt_display')

    class Meta:
        model = RoomType
        fields = ('id', 'type_rt', 'price_rt')


# Registration
class RegistrationRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'number_room')


class RegistrationSerializer(serializers.ModelSerializer):
    user_reg = RegComUserSerializer()
    hotel_reg = RegComHotelSerializer()
    rt_reg = RegComRoomTypeSerializer()
    room_reg = RegistrationRoomSerializer()
    status_reg_reg = serializers.CharField(source='get_status_reg_reg_display')
    status_pay_reg = serializers.CharField(source='get_status_pay_reg_display')

    class Meta:
        model = Registration
        fields = '__all__'


# Comment
class CommentRoomSerializer(serializers.ModelSerializer):
    hotel_r = RegComHotelSerializer()
    rt_r = RegComRoomTypeSerializer()
    status_room = serializers.CharField(source='get_status_room_display')

    class Meta:
        model = Room
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user_com = RegComUserSerializer()
    room_com = CommentRoomSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
```
* `urls.py`

Add urls:
```python
from django.urls import path

from .views import RegistrationViewSet, CommentViewSet

urlpatterns = [
    path('reg/', RegistrationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('reg/<int:pk>/', RegistrationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('com/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('com/<int:pk>/', RegistrationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
```

## API
Structure of API:
* **hotel**
* **account_app**
* **hotel_app**
* **reg_com_app**

### hotel urls
`doc/swagger/`
* GET

Swagger documentation.

`doc/redoc/`
* GET

Redoc documentation.

`auth/token/`
* POST

Get refresh and access token for user.

`auth/token/refresh/`
* POST

Update refresh and access token for user.

`auth/`
* GET

Get url for working with user.

### account_app urls
`account/user/`
* GET (admin, owner)

List of users.

* POST (allow any)

Create an account.

`account/user/<int:pk>/`
* GET (admin, owner)

Get the user info.

* PUT, DELETE (admin, owner)

Change the user info.

### hotel_app urls
`hotel/`
* GET (allow any)

Get list of hotels.

`hotel/<int:pk>/`
* GET (allow any)

Get the hotel.

* POST, PUT, DELETE (admin)

Change the hotel info.

`hotel/room_type/<int:pk>/`
* GET (allow any)

Get the room type.

* POST, PUT, DELETE (admin)

Change the room type info.

`hotel/room_type/room/<int:pk>/`
* GET (allow any)

Get the room.

* POST, PUT, DELETE (admin)

Change the room info.

### reg_com_app urls
`reg/`
* GET, POST (admin, owner)

Get list of registrations.

`reg/<int:pk>/`
* GET, PUT, DELETE (admin, owner)

Get or change registration info.

`com/`
* GET, POST (admin, owner)

Get list of comments.

`com/<int:pk>/`
* GET, PUT, DELETE (admin, owner)

Get or change comment info.