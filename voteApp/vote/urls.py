from django.contrib import admin
from django.urls import path, include
from vote import views

urlpatterns = [
    path('', views.index , name = "home"),
    path('login', views.loginUser , name = "login"),
    path('logout', views.logoutUser , name = "logout"),
    path('candidate-voted/<int:pk>', views.Vote, name="candidate_vote"),

]
