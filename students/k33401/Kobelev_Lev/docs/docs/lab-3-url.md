# URLs

В `urls.py`:

``` python
urlpatterns = [
    path('scenarios/', ScenarioListAPIView.as_view()),
    path('scenarios/<int:pk>/', ScenarioAPIView.as_view()),
    path('scenarios/<int:pk>/update/', ScenarioUpdateAPIView.as_view()),
    path('scenarios/<int:pk>/delete/', ScenarioDestroyAPIView.as_view()),
    path('scenarios/<int:scenario>/likes/update/', ScenarioLikesUpdateAPIView.as_view()),
    path('scenarios/create/', ScenarioCreateAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
    path('tags/create/', TagCreateAPIView.as_view()),
    path('game_systems/', GameSystemListAPIView.as_view()),
    path('game_systems/create/', GameSystemCreateAPIView.as_view()),
    path('scenarios/<int:scenario>/reviews/create/', ReviewCreateAPIView.as_view()),
    path('scenarios/<int:scenario>/reviews/<int:review>/update/', ReviewUpdateAPIView.as_view()),
    ]
```