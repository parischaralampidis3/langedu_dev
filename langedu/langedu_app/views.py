from rest_framework import generics
from .serializers import TextQuestionContainerSerializer, TextQuestionSerializer
from .models import TextQuestionContainer, TextQuestion

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