from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("register/", views.UsersRegister.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("logout/", views.Logout.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    # path("<int:pk>/", views.UsersDetail.as_view()),
]
