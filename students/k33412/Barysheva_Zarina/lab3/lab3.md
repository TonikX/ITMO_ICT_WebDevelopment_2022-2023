# Лабораторная работа №3
Реализовать сайт, используя фреймворк Django 3, Django REST Framework, Djoser

## Вариант
Вариант с курса по фронтенд-разработке:
#### Платформа для поиска профессиональных мероприятий

## Функционал
* Авторизация и регистрация через djoser
* Получение списка мероприятний
* Регистрация мероприятия
* Регистрация пользователя на мероприятие
* Список пользователей, зарегистрированных на определенное мероприятие
* Список мероприятий, на которые зарегистрирован пользователь
* Фильтрация всего списка мероприятий по *типу* мероприятия и/или *месту проведения*

## Структура
`lab3_Barysheva` - Проект Django

`merofond` - Приложение Django

### Проект
Настройки аутентификафии по токену и рендера в браузере в `settings.py`
```
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
    "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": (
    "rest_framework.renderers.JSONRenderer",'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}
```

Паттерны url в `urls.py`, подключены эндпойнты djoser
```
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("merofond.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]

```

### Приложение
Паттерны url в `urls.py`
```
urlpatterns = [
    path('users/', UsersViewSet.as_view()),
    path('event/create/', EventCreateAPIView.as_view()),
    path('event/list/', EventListAPIView.as_view()),
    re_path(r'event/(?P<event_id>[0-9]+)/$', EventAPIView.as_view()),
    re_path(r'event/list/filter/(?P<type>\w*)/(?P<location>\w*)/$', EventFilterListAPIView.as_view()),
    path('event/type/', EventTypeListAPIView.as_view()),
    re_path(r'event/type/(?P<type_id>[0-9]+)/$', EventTypeAPIView.as_view()),
    re_path(r'event/location/(?P<location_id>[0-9]+)/$', LocationAPIView.as_view()),
    path('event/location/', LocationListAPIView.as_view()),
    re_path(r'user/(?P<user_id>[0-9]+)/$', UserAPIView.as_view()),
    re_path(r'user/(?P<user_id>[0-9]+)/events/$', RegisrationForUserListAPIView.as_view()),
    re_path(r'event/(?P<event_id>[0-9]+)/users/$', RegisrationForEventListAPIView.as_view()),
    path('event/reg/', RegistrationCreateAPIView.as_view()),
]
```

Модели в `models.py`
```
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)

class Location(models.Model):
    title = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

class EventType(models.Model):
    title = models.CharField(max_length=50, unique=True)

class Event(models.Model):
    organizer = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    datetime = models.DateField()
    event_type = models.ForeignKey(EventType,on_delete=models.CASCADE)

class Registration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

```

Сериализаторы в `serializers.py`
```
class MeroUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ["id", "username"]

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'title', 'address']

class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = ['id', 'title']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'organizer', 'title', 'description', 'location', 'datetime', 'event_type']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'user', 'event']
```

Представления в `views.py`
```
class UsersViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = MeroUserSerializer

class UserAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeroUserSerializer

    def get_queryset(self):
        cur_user = self.kwargs['user_id']
        return User.objects.get(pk=cur_user)


class EventAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        cur_event = self.kwargs['event_id']
        return Event.objects.filter(pk=cur_event)

class EventCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventFilterListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        cur_type = self.kwargs['type']
        cur_location = self.kwargs['location']
        events_cur_type = Event.objects.filter(event_type__title=cur_type)
        events_cur_location = Event.objects.filter(location__title=cur_location)
        if events_cur_location.exists() and events_cur_type.exists():
            return events_cur_location.intersection(events_cur_type)
        if events_cur_location.exists() or events_cur_type.exists():
            return events_cur_location.union(events_cur_type)
        
        return Event.objects.all()   


class EventTypeAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventTypeSerializer
    def get_queryset(self):
        cur_type = self.kwargs['type_id']
        return EventType.objects.filter(id=cur_type)


class EventTypeListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class LocationAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LocationSerializer
    def get_queryset(self):
        cur_location = self.kwargs['location_id']
        return Location.objects.filter(pk=cur_location)

class LocationListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class RegisrationForUserListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        cur_user = self.kwargs['user_id']
        regs = Registration.objects.filter(user__id=cur_user)
        events_id = []
        for reg in regs:
            events_id.append(reg.event.pk)
        return Event.objects.filter(pk__in=events_id)
    
class RegisrationForEventListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeroUserSerializer

    def get_queryset(self):
        cur_event = self.kwargs['event_id']
        regs = Registration.objects.filter(event__id=cur_event)
        users_id = []
        for reg in regs:
            users_id.append(reg.user.pk)
        return User.objects.filter(id__in=users_id)
    
class RegistrationCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
```