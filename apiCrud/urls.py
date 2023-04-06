from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path("",VCardView.as_view()),
    path("<int:id>/",VCardDetails.as_view()),
    path("login/",MyTockenObjectPaieView.as_view()),
    path("login/refresh/",TokenRefreshView.as_view()),
    path("register/",RegisterView.as_view()),
]
