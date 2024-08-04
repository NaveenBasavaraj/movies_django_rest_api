from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()


class StreamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    about = serializers.CharField(max_length=150)
    website = serializers.URLField(max_length=100)
    allows_multi_users = serializers.BooleanField(default=False)
    create_ts = serializers.DateTimeField(auto_now_add=True)
    modified_ts = serializers.DateTimeField(auto_now=True)


class ReviewSerializer(serializers.Serializer):
    rating = serializers.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    movie = serializers.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    description = serializers.CharField(max_length=100)
    review = serializers.TextField()
    is_active = serializers.BooleanField(default=True)
    create_ts = serializers.DateTimeField(auto_now_add=True)
    modified_ts = serializers.DateTimeField(auto_now=True)