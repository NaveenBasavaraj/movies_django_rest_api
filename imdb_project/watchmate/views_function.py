from watchmate.models import Movie, SteamingPlatform, Review
from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchmate.api.serializers import MovieSerializer


@api_view()
def movie_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_detail_api_view(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view()
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = MovieSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view()
def review_detail_api_view(request, pk):
    review = Review.objects.get(pk=pk)
    serializer = MovieSerializer(review)
    return Response(serializer.data)


@api_view()
def streaming_platform_list_api_view(request):
    sps = SteamingPlatform.objects.all()
    serializer = MovieSerializer(sps, many=True)
    return Response(serializer.data)

@api_view()
def streaming_platform_detail_api_view(request, pk):
    sp = SteamingPlatform.objects.get(pk=pk)
    serializer = MovieSerializer(sp)
    return Response(serializer.data)