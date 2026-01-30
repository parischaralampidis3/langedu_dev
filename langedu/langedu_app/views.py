from rest_framework import generics
from .serializers import TextQuestionContainerSerializer, TextQuestionSerializer, TextResponseSerializer
from .models import TextQuestionContainer, TextQuestion, TextResponse
from django.shortcuts import get_object_or_404
# Create your views here.
#texquestion container views
class TextQuestionContainerListCreateView(generics.ListCreateAPIView):
    queryset = TextQuestionContainer.objects.all()
    serializer_class = TextQuestionContainerSerializer

class TextQuestionContainerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TextQuestionContainer.objects.all()
    serializer_class = TextQuestionContainerSerializer

#textquestion views


class TextQuestionListCreateView(generics.ListCreateAPIView):
    queryset = TextQuestion.objects.all()
    serializer_class = TextQuestionSerializer

class TextQuestionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TextQuestion.objects.all()
    serializer_class = TextQuestionSerializer 


#textresponse views

class TextResponseListCreateView(generics.ListCreateAPIView):
    queryset = TextResponse.objects.all()
    serializer_class = TextResponseSerializer

class TextResponseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TextResponse.objects.all()
    serializer_class = TextResponseSerializer

    
class TextResponseListCreateView(generics.ListCreateAPIView):
    serializer_class = TextResponseSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return TextResponse.objects.select_related('text_question').filter(text_question__id=question_id)

    def perform_create(self, serializer):
        question_id = self.kwargs['question_id']
        text_question = get_object_or_404(TextQuestion, id=question_id)
        serializer.save(text_question=text_question)