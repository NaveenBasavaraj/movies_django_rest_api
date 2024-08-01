from django.urls import path
from views import movie_list_json, movie_details_json

urlpatterns = [
    path("list/", movie_list_json, name="movie-list"),
    path("list/<int:id>", movie_details_json, name="movie-details"),
]