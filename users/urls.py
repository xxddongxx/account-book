from django.urls import path

from users import views

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("register/", views.UsersRegister.as_view()),
    path("login/", views.Login.as_view()),
    path("logout/", views.Logout.as_view()),
    path("<int:pk>/", views.UsersDetail.as_view()),
]
