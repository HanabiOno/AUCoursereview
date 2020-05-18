from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.template import loader
from django.urls import reverse
from django.views import generic
from .forms import *
from django.db.models import Avg

class IndexView(generic.ListView):
    template_name = 'reviews/index.html'
    context_object_name = 'latest_course_list'

    def get_queryset(self):
        """Return all published courses."""
        return Course.objects.order_by('course_name')

class DetailView(generic.DetailView):
    model = Course
    template_name = 'reviews/detail.html'

    '''
    #If we want to add average rating
    reviews = Review.objects.all().order_by("-comment")
    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average, 2)
'''
    
class ResultsView(generic.DetailView):
    model = Course
    template_name = 'reviews/results.html'

def review(request):
    if request.user.is_authenticated:
        course_list = list(Course.objects.all()) 
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.course = request.POST["course"] 
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.save()
                return redirect("reviews:review")
        else:
            form = ReviewForm() 
            return render(request, 'reviews/review.html', {"form": form})
    else:
        return redirect("accounts:login")

