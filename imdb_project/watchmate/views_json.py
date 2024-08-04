from django.http import JsonResponse
from django.shortcuts import render
from watchmate.models import Movie

# json response based views ie. not using framework

def movie_list_json(request):
    '''
    json response without using any framework
    '''
    movies = Movie.objects.all()
    data = {
        'movies': list(movies)
    }
    return JsonResponse(data)

def movie_details_json(request, id):
    '''
    json response without using any framework
    '''
    movie = Movie.objects.get(id=id)
    data = {
        'movie': movie.title,
        'description':movie.description,
        'active':movie.is_active
    }
    return JsonResponse(data)