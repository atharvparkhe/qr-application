from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('read/', views.readQR, name="read"),
    path('generate/', views.generateQR, name="generate"),
]