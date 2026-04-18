from django.db import models
from django.contrib.auth.models import User


class CountryManager(models.Manager):
    def high_salary_countries(self):
        return self.filter(salary__gte=8)


class Region(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='countries')
    description = models.TextField()
    safety = models.IntegerField()
    salary = models.IntegerField()
    quality_of_life = models.IntegerField()
    cost_of_living = models.IntegerField()
    healthcare = models.IntegerField()
    english_friendly = models.IntegerField()
    image = models.URLField(blank=True)

    objects = CountryManager()

    def __str__(self):
        return self.name


class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preferences')
    current_country = models.CharField(max_length=100)
    preferred_region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    safety_weight = models.IntegerField(default=5)
    salary_weight = models.IntegerField(default=5)
    quality_weight = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.user.username} preferences"


class FavoriteCountry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='favorited_by')

    def __str__(self):
        return f"{self.user.username} - {self.country.name}"