from django.urls import path
from . import views

urlpatterns = [
    path('', views.anogram_view, name='anogram'),
        ]
