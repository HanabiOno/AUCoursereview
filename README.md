# AUCourse review website

[Assignment 6] (https://advprog.auc-computing.nl/assignment6.html) for Advanced Programming: Build a website

> To run the server follow these steps:
>   - workon django (go to a django supporting env)
>   - pip install django-crispy-forms

> go to the directory mysite
>   - python manage.py runserver 0:8000

> go to the following address in your browser
>   - http://localhost:8764/


###Review app
The review app gives a [list of all courses] (http://localhost:8764/reviews/) and by selecting a course you will see a [detailed overview] (http://localhost:8764/reviews/1/) on the course including the reviews. If you want to submit a review you can go to the [reviews page] (http://localhost:8764/reviews/review/). There you will select a existing course (on our website) add a comment and a rating.

> Format for the course overview is under mysite/reviews/templates/reviews/index.html
> Format for each course page is under mysite/reviews/templates/reviews/detail.html
> Format for the review page is under mysite/reviews/templates/reviews/review.html

###The home page
From the home page you can go to either the HUM, SCI, SSC, ACC or review page. From the first three pages you can click on the placemat for each major to select a course you would like to review or see the reviews on.

> For now we will only make 5 course pages for each major.
