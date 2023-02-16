from django.urls import path

from . import views
from .views import kit_create


app_name = "cross"

urlpatterns = [
    # Главная страница
    path("", views.index),
    path("create/", views.kit_create, name="kit_create"),
    path("kit", views.kit_list, name="kit_list"),
    path("kit/<slug:slug>/", views.kit_detail, name="kit_detail"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("kit/<int:post_id>/edit/", views.kit_edit, name="kit_edit"),
]
