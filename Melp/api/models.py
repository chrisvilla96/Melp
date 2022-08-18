from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Restaurant(models.Model):
    """Model for Restaurant Data"""

    id = models.CharField(primary_key=True, editable=False, max_length=254)
    rating = models.IntegerField(
        default=0, 
        validators = [MinValueValidator(0), MaxValueValidator(5)]
    )
    name = models.CharField(max_length=254)
    site = models.TextField(max_length=1000)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    street = models.TextField(max_length=1000)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=16, decimal_places=13)
    lng = models.DecimalField(max_digits=16, decimal_places=13)

    def __str__(self) -> str:
        return self.name