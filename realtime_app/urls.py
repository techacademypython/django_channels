from django.urls import path
from . import views

urlpatterns = [
    path('', views.RealtimeIndex.as_view(), name="main"),
]
