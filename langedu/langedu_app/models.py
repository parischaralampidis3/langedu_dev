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
    creeated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)