from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('task-list/', views.taskList, name="task-list"),
    path('hi', views.test),
    path('bye', views.new),
]
