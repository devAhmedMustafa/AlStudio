from django.urls import path
from .views import DesignsListAPI, DesignAPI, LoveAPI

urlpatterns = [
    path('designs/', DesignsListAPI.as_view()),
    path('designs/<uuid>', DesignAPI.as_view()),
    path('designs/loved/', LoveAPI.as_view())
]
