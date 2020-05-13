from django.contrib import admin
from .models import Course, Review, Question, Choice

admin.site.register(Course)
admin.site.register(Review) 
admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
