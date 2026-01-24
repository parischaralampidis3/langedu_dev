from django.urls import path
from .views import (
    TextQuestionContainerListCreateView,
    TextQuestionContainerRetrieveUpdateDestroyView,
    TextQuestionListCreateView,
    TextQuestionRetrieveUpdateDestroyView
    )

urlpatterns = [
    
        path('container/', TextQuestionContainerListCreateView.as_view(), name='textQuestionContainerListCreate'),
        path('container/<int:pk>/', TextQuestionContainerRetrieveUpdateDestroyView.as_view(), name='textQuestionContainerRetrieveUpdateDestroy'),
       
        path('question/', TextQuestionListCreateView.as_view(), name='textQuestionListCreate'),
        path('question/<int:pk>/', TextQuestionRetrieveUpdateDestroyView.as_view(), name='textQuestionRetrieveUpdateDestroy')  
    ]