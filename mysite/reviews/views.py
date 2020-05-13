from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course, Review
from django.template import loader
from django.urls import reverse
from django.views import generic

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

def review(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    try:
        selected_review = course.review_set.get(pk=request.POST['review'])
    except (KeyError, Review.DoesNotExist):
        # Redisplay the course voting form.
        return render(request, 'reviews/detail.html', {
            'course': course,
            'error_message': "You didn't write a review.",
        })
    else:
        selected_review.reviews += 1
        selected_review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:results', args=(course.id,)))
    
# Create your views here.
