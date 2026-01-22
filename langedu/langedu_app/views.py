from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from rest_framework import generics
from serializers import TextQuestionContainerSerializer, TextQuestionSerializer
from models import TextQuestionContainer, TextQuestion

# Create your views here.

class TextQuestionContainerListCreateView(generics.ListCreateAPIView):
    queryset = TextQuestionContainer.objects.all()
    serializer_class = TextQuestionContainerSerializer

class TextQuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TextQuestion.objects.all()
    serializer_class = TextQuestionSerializer

def textQuestionContainerList(request):
    textQuestionContainer = TextQuestionContainer.objects.all()
    return render(request, './textQuestionContainer/textQuestionContainer.html',{'textQuestionContainer':textQuestionContainer})

def textQuestion(request, pk):
    textQuestion = get_object_or_404(TextQuestion, pk=pk)
    return render(request, './textQuestion/textQuestion.html',{'textQuestion':textQuestion})


def textQuestionList(request):
    textQuestionList = TextQuestion.objects.all()
    return render(request, './textQuestionList/textQuestionList.html',{'textQuestionList':textQuestionList})

