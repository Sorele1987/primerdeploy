from django.urls import URLPattern, path
from .views import DirectionAPIView


urlpatterns = [
    path('', DirectionAPIView.as_view()),
]
