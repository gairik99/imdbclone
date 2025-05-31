from django.db import models


# Create your models here.
class StreamingService(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self):
        return f"name: {self.name},"



class WatchList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    active = models.BooleanField(default=True)
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"title: {self.title} "