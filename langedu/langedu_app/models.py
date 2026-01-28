from django.db import models

    

class TextQuestionContainer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='Default question container description')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title
    

class TextQuestion(models.Model):
    question_number_id = models.IntegerField()
    title = models.CharField(max_length= 200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    text_question_container = models.ForeignKey(
        TextQuestionContainer,
        on_delete = models.CASCADE,
        related_name='text_questions'
    )

    class Meta:
        ordering = ['question_number_id']
        constraints = [
            models.UniqueConstraint(
                fields=['question_number_id', 'text_question_container'],
                name='unique_question_per_container'
            )
        ]

    def __str__(self):
        return self.title

class TextResponse(models.Model):
    response_number_id = models.IntegerField()
    response_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    text_question = models.ForeignKey(
        TextQuestion,
        on_delete = models.CASCADE,
        related_name='text_responses'
    )
    
    class Meta:
        ordering = ['response_number_id']
        constraints = [
             models.UniqueConstraint(
                 fields = ['response_number_id', 'text_question'],
                 name = 'unique_response_per_question'
             )
        ]

    def __str__(self):
        return self.response_text[:50]  # Return first 50 characters of the response text
        

        
        