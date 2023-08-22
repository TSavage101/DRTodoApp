from django.urls import path

from .views import AllTasks, SingleTask

urlpatterns = [
    path('tasks/', AllTasks.as_view(), name='tasks'),
    path('tasks/<int:pk>/', SingleTask.as_view(), name='atask'),
]
