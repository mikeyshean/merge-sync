from django.urls import path
from . import views

app_name = 'merge'

urlpatterns = [
    path('', views.index, name='index')
]
