from rest_framework import serializers
from .models import TextQuestionContainer, TextQuestion, TextResponse

class TextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQuestion
        fields = ['id', 'question_number_id', 'title', 'is_active', 'created_at', 'updated_at']


class TextQuestionContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQuestionContainer
        fields = ['id','title','description', 'is_active', 'created_at', 'updated_at']


class TextResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextResponse
        fields = ['id',  'response_text', 'created_at', 'updated_at']