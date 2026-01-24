from django.urls import path
from .views import (
    textQuestionContainerList,
    textQuestion,
    textQuestionList
    )

urlpatterns = [
        #path('', textQuestionContainerList, name='textQuestionContainerList'), 
        path('question/<int:pk>/', textQuestion.as_view(), name='textQuestion'),
        path('list/', textQuestionList.as_view(), name='textQuestionList')  
    ]