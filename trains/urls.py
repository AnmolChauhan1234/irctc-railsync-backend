from django.urls import path
from .views import TrainAdminView, TrainSearchView

urlpatterns = [
    path("/", TrainAdminView.as_view()),          # Admin
    path("search/", TrainSearchView.as_view()),  # User
]
