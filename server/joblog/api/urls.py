from django.urls import path
from .views import get_Jobs


urlpatterns = [
    path('jobs/', get_Jobs, name='get_Jobs')
]