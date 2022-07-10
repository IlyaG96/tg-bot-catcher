from django.urls import include, path

urlpatterns = [
    path('', include('tg_catcher.urls')),
]
