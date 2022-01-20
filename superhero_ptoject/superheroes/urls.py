from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    path('index/', views.index, name = 'index')
]