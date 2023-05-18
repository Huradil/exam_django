from .models import News,NewsStatus,CommentStatus,Comment,Status
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    reactions = serializers.ReadOnlyField(source='get_reactions')

    class Meta:
        model=News
        fields="__all__"


class CommentSerializer(serializers.ModelSerializer):
    reactions = serializers.ReadOnlyField(source='get_reactions')

    class Meta:
        model = Comment
        fields = "__all__"


class NewsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStatus
        fields = "__all__"


class CommentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentStatus
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


