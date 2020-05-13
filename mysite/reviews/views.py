from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course

def index(request):
    latest_course_list = Course.objects.order_by('course_name')
    context = {'latest_course_list': latest_course_list}
    return render(request, 'reviews/index.html', context)

def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'reviews/detail.html', {'course': course})

def results(request, course_id):
    reviews = "You're looking at the reviews of course: %s."
    return HttpResponse(response % course_id)

def review(request, course_id):
    return HttpResponse("You're reviewing the course %s." % course_id)

# Create your views here.
