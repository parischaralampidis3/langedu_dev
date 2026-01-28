from rest_framework import generics
from .serializers import TextQuestionContainerSerializer, TextQuestionSerializer, TextResponseSerializer
from .models import TextQuestionContainer, TextQuestion, TextResponse

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
    
    