from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(required=True, format="%s", input_formats=["%Y-%m-%d %H:%M:%S"])

    class Meta:
        model = models.Post
        fields = ('id', 'post_id', 'timestamp',)
