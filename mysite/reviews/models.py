from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    catalogue_nr = models.CharField(max_length=10)
    def __str__(self):
        return self.course_name

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    rating = models.FloatField(default=0)
    def __str__(self):
        return self.comment
        #return self.user.username

# Create your models here.
