from django.db import models


# Create your models here.
class Product(models.Model):
    SIZE_CHOICES = [
        ('1', 'Small'),
        ('2', 'Medium'),
        ('3', 'Large'),
        ('4', 'Extra Large'),
    ]

    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    sold_count = models.PositiveIntegerField(default=0)
    rating_count = models.PositiveIntegerField(default=0)
    short_description = models.TextField()
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    weight = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
