from django import forms
from .models import *

# course add form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'catalogue_nr')
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("course", "comment", "rating")
