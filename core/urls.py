from django.urls import path

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('create/', home, name='create'),
    path('update/<int:pk>/', home, name='update'),
]
