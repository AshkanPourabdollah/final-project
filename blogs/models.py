from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=20)
    short_description = models.TextField()
    long_description = models.TextField()
    author = models.CharField(max_length=255)

    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
