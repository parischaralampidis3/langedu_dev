from django.urls import path
from .views import (
    TextQuestionContainerListCreateView,
    TextQuestionContainerRetrieveUpdateDestroyView,
    TextQuestionListCreateView,
    TextQuestionRetrieveUpdateDestroyView,
    TextResponseListCreateView,
    TextResponseRetrieveUpdateDestroyView
    )

urlpatterns = [
    
        path('container/', TextQuestionContainerListCreateView.as_view(), name='textQuestionContainerListCreate'),
        path('container/<int:pk>/', TextQuestionContainerRetrieveUpdateDestroyView.as_view(), name='textQuestionContainerRetrieveUpdateDestroy'),
       
        path('question/', TextQuestionListCreateView.as_view(), name='textQuestionListCreate'),
        path('question/<int:pk>/', TextQuestionRetrieveUpdateDestroyView.as_view(), name='textQuestionRetrieveUpdateDestroy'),


        path('response/', TextResponseListCreateView.as_view(), name='textResponseListCreate'),
        path('response/<int:pk>/', TextResponseRetrieveUpdateDestroyView.as_view(), name='textResponseRetrieveUpdateDestroy'),

        path('question/<int:question_id/responses>/', TextResponseListCreateView.as_view(), name= 'textResponseListCreate')
        

    ]
