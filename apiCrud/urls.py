from django.urls import path,include
from .views import VCardView
urlpatterns = [
    path("",VCardView.as_view()),
]
