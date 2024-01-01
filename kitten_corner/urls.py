from django.urls import path

from kitten_corner import views


app_name = "kitten_corner"
urlpatterns = [
    path("", views.index, name="index"),
]
