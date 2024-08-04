from watchmate.models import Movie, SteamingPlatform, Review
from rest_framework.response import Response
from watchmate.api.model_serializers import MovieSerializer, StreamSerializer, ReviewSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewDetail(mixins.RetrieveModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)(request, *args, **kwargs)