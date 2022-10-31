from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("rooms/", views.rooms_view, name="rooms"),
    path("rooms/<room_name>", views.room_view, name="room"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh")
]