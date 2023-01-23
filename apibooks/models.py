from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


class Books(models.Model):
    name = models.CharField(unique=True, max_length=200)
    author = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    category = models.CharField(max_length=200)
    image = models.ImageField(null=True, upload_to="images'")

    @property
    def avg_rating(self):
        ratings = self.review_set.all().values_list("rating", flat=True)
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0

    @property
    def review_user(self):
        ratings = self.review_set.all().values_list("rating", flat=True)
        if ratings:
            return len(ratings)
        else:
            return 0

    def __str__(self):
        return self.name
