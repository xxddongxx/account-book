from django.urls import path

from accounts import views

urlpatterns = [
    path("", views.Accounts.as_view()),
    path("<int:pk>/", views.AccountDetail.as_view()),
    path("restoration/", views.AccountRestoration.as_view()),
    path("restoration/<int:pk>/", views.AccountRestorationDetail.as_view()),
]
