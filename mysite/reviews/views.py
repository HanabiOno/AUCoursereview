from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course, Review
from django.template import loader
from django.urls import reverse
from django.views import generic
from .forms import *

class IndexView(generic.ListView):
    template_name = 'reviews/index.html'
    context_object_name = 'latest_course_list'

    def get_queryset(self):
        """Return all published courses."""
        return Course.objects.order_by('course_name')

class DetailView(generic.DetailView):
    model = Course
    template_name = 'reviews/detail.html'

class ResultsView(generic.DetailView):
    model = Course
    template_name = 'reviews/results.html'

def review(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.course = request.POST["course %s"] 
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.course = course
                data.save()
                return redirect("reviews:review", pk)
        else:
            form = ReviewForm()
        return render(request, 'reviews/review.html', {"form": form})
    else:
        return redirect("accounts:login")

