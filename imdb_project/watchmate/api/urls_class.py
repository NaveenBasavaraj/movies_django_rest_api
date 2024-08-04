from django.urls import path
from watchmate.views_class import ReviewDetail, ReviewList


urlpatterns = [
    path('list/', ReviewList.as_view(), name='review-list'),
    path('list/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]