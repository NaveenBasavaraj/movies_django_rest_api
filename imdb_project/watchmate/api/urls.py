from django.urls import path
from watchmate.views_json import movie_list_json, movie_details_json
from watchmate.views_function import (movie_list_api_view, movie_detail_api_view,
                                    streaming_platform_list_api_view,streaming_platform_detail_api_view,
                                    review_list_api_view, review_detail_api_view)


urlpatterns = [

    #function based views 
    path("func-list/", movie_list_api_view, name="movie-func-list"),
    path("func-list/<int:id>", movie_detail_api_view, name="movie-func-details"),
    path("func-stream-list/", streaming_platform_list_api_view, name="stream-func-list"),
    path("func-stream-list/<int:id>", streaming_platform_detail_api_view, name="stream-func-details"),
    path("func-review-list/", review_list_api_view, name="review-func-list"),
    path("func-review-list/<int:id>", review_detail_api_view, name="review-func-details"),
    # json based views
    path("list/", movie_list_json, name="movie-list"),
    path("list/<int:id>", movie_details_json, name="movie-details"),
]