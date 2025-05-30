from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    gross_revenue = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.release_date}) , Rating: {self.rating}, Gross Revenue: ${self.gross_revenue}"
