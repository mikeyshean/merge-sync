from django.urls import path
from backend.merge import views

app_name = 'merge'

urlpatterns = [
    path('', views.index, name='index')
]
