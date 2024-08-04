from rest_framework import serializers
from watchmate.models import Movie, SteamingPlatform, Review

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.get_or_create(**validated_data)


class StreamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    about = serializers.CharField()
    website = serializers.URLField()
    allows_multi_users = serializers.BooleanField()

    def create(self, validated_data):
        return SteamingPlatform.objects.get_or_create(**validated_data)


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField(min_value=1, max_value=5)
    movie = serializers.CharField()
    description = serializers.CharField()
    review = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Review.objects.get_or_create(**validated_data)
