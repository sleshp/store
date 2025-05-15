from rest_framework import serializers
from .models import Feedback, ReferenceMaterial


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('user', 'created', 'text', 'rating', 'status')
        read_only_fields = ('created',)


class ReferenceMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceMaterial
        fields = ('title', 'content_type', 'content')