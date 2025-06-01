from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class StreamingService(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self):
        return f"name: {self.name},"

class Review(models.Model):
    # review_user = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    watchlist = models.ForeignKey(
        'WatchList', related_name='reviews', on_delete=models.CASCADE,null=True, blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"title: {self.watchlist.title}, rating: {self.rating}"


class WatchList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    active = models.BooleanField(default=True)
    release_date = models.DateField(auto_now_add=True)
    service= models.ForeignKey(
        StreamingService, related_name='watchlists', on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"title: {self.title} "