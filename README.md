# AUCourse review website

[Assignment 6] (https://advprog.auc-computing.nl/assignment6.html) for Advanced Programming: Build a website

> To run the server follow these steps:
>   - workon django (go to a django supporting env)
>   - pip install django-crispy-forms

> go to the directory mysite
>   - python manage.py runserver 0:8000

> go to the following address in your browser
>   - http://localhost:8764/


###[The home page] ((http://localhost:8764/) STILL NEEDS TO BE DONE
From the home page you can go to either the HUM, SCI, SSC, ACC or review page. From the first three pages you can click on the placemat for each major to select a course you would like to review or see the reviews on.

###[Review app] (http://localhost:8764/reviews/
The review app gives a [list of all courses] (http://localhost:8764/reviews/) and by selecting a course you will see a [detailed overview] (http://localhost:8764/reviews/1/) on the course including the reviews. If you want to submit a review you can go to the [reviews page] (http://localhost:8764/reviews/review/). There you will select a existing course (on our website) add a comment and a rating.

- adding other questions STILL NEEDS TO BE DONE

> Format for the course overview is under mysite/reviews/templates/reviews/index.html

> Format for each course page is under mysite/reviews/templates/reviews/detail.html

> Format for the review page is under mysite/reviews/templates/reviews/review.html

###The polls app 
> The polls app can be considered as a main app 
Initially we started the website by following the Django tutorial making a polls app which at first seemed to be a good approach for our review website however it turned out to make it more complicated.This is because for a review you need the answers to be assigned to a review. As we would have 4 models (Question, Choice, Course and Review) this made it unneccesarily complicated. That is why we started over using [crispy-forms] (https://django-crispy-forms.readthedocs.io/en/latest/).
> If you are interested in our start up with the polls app anyways you can check it out [here] (http://localhost:8764/polls/)

###[The accounts app] (http://localhost:8764/accounts/register/)
The accounts app will make it possible to [login] (http://localhost:8764/accounts/login/), [logout] (http://localhost:8764/accounts/logout/) and to make the reviews connected to a user.
- connecting accounts app to reviews STILL NEEDS TO BE DONE

> For now we will only make 5 course pages for each major.

