from django.urls import path

from . import views


app_name = "cross"

urlpatterns = [
    # Главная страница
    path("", views.index),
    path("kit", views.kit_list, name="kit_list"),
    path("kit/<slug:slug>/", views.kit_detail, name="kit_detail"),
    path("profile/<str:username>/", views.profile, name="profile"),
]
