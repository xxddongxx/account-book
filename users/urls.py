from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("<int:pk>/", views.UsersDetail.as_view()),
    path("register/", views.UsersRegister.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
