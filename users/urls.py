from django.urls import path, include
from .views import UserDetailAPI,RegisterUserAPIView, UserNameAPI, UserMediaAPI


urlpatterns = [
  path("get-details/",UserDetailAPI.as_view()),
  path('register/',RegisterUserAPIView.as_view()),
  path("getusername/<int:pk>/", UserNameAPI.as_view()),
  path("user_profile/<username>/", UserMediaAPI.as_view()),
]
