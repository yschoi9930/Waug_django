from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model) :
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject

class Comment(models.Model) :
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)