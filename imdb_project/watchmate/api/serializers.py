from rest_framework import serializers
from watchmate.models import Movie, SteamingPlatform, Review

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.get_or_create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.is_active = validated_data.get("is_active", instance.is_active)


class StreamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    about = serializers.CharField()
    website = serializers.URLField()
    allows_multi_users = serializers.BooleanField()

    def create(self, validated_data):
        return SteamingPlatform.objects.get_or_create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.about = validated_data.get("about", instance.about)
        instance.website = validated_data.get("website", instance.website)
        instance.allows_multi_users = validated_data.get("allows_multi_users", instance.allows_multi_users)

class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField(min_value=1, max_value=5)
    movie = serializers.CharField()
    description = serializers.CharField()
    review = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Review.objects.get_or_create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.rating = validated_data.get("about", instance.rating)
        instance.description = validated_data.get("description", instance.description)
        instance.review = validated_data.get("review", instance.review)
        instance.is_active = validated_data.get("is_active", instance.is_active)

