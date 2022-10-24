from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Country(models.Model):
    name = models.CharField('Country name', max_length=64, unique=True)
    slug = models.SlugField('Country link', max_length=64, unique=True)
    description = models.CharField('Country description', max_length=1000, null=True)
    image = models.ImageField('Image of country', upload_to='images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('country_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    description = models.CharField(max_length=1024, db_index=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True)
    price_per_person = models.FloatField()
    nights_count = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tour_details_url', kwargs={'slug': self.slug})


class TourImage(models.Model):
    name = models.CharField('Tour image name', max_length=64, unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


Customer = get_user_model()


class TourConducting(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_start = models.DateField()
    is_verified = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    tourists = models.IntegerField(default=1)
    contact_info = models.TextField()
    review_text = models.TextField(null=True, default=None, blank=True)
    rate = models.IntegerField(null=True, default=None, blank=True)

    def __str__(self):
        status = 'PAID' if self.is_paid else 'VERIFIED' if self.is_verified else 'NEW'
        return f"[{status}] {self.tour} / {self.customer}"
