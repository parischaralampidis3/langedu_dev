from django.contrib import admin

# Register your models here.
from .models import TextQuestionContainer, TextQuestion

admin.site.register(TextQuestionContainer)
admin.site.register(TextQuestion)

