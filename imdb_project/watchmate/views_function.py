from watchmate.models import Movie, SteamingPlatform, Review
from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchmate.api.serializers import MovieSerializer, StreamSerializer, ReviewSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serialized_request_data = MovieSerializer(data=request.data)
        if serialized_request_data.is_valid():
            serialized_request_data.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def movie_detail_api_view(request, pk):
    if request.method == "GET":
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == 'PUT':
        serialized_request_data = MovieSerializer(data=request.data)
        if serialized_request_data.is_valid():
            serialized_request_data.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serialized_request_data = ReviewSerializer(data=request.data)
        if serialized_request_data.is_valid():
            serialized_request_data.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def review_detail_api_view(request, pk):
    if request.method == 'GET':
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    if request.method == 'PUT':
        serialized_request_data = ReviewSerializer(data=request.data)
        if serialized_request_data.is_valid():
            serialized_request_data.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        movie = Review.objects.get(pk=pk)
        movie.delete()


@api_view(['GET', 'POST'])
def streaming_platform_list_api_view(request):
    if request.method == 'GET':
        sps = SteamingPlatform.objects.all()
        serializer = StreamSerializer(sps, many=True)
        return Response(serializer.data)
    

@api_view(['GET','PUT','DELETE'])
def streaming_platform_detail_api_view(request, pk):
    sp = SteamingPlatform.objects.get(pk=pk)
    serializer = StreamSerializer(sp)
    return Response(serializer.data)