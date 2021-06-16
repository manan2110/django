from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('task-list/', views.taskList, name="task-list"),
    path('hi', views.test),
    path('hi2', views.test2),
    path('bye', views.new),
    path('bye2', views.new2),
    path('gettoken/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refreshtoken/', TokenRefreshView.as_view(), name="token_refresh"),
    path('verifytoken/', TokenVerifyView.as_view(), name="verify_token")
]
