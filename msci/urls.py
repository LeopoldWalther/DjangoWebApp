from django.urls import path
from msci import views

urlpatterns = [
    path('', views.msci , name='msci'),
]