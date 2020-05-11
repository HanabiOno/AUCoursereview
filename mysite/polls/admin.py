from django.contrib import admin

from .models import Choice, Question, Course, Review

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date') #this line is probably not necessary for us
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Course)
admin.site.register(Review)
