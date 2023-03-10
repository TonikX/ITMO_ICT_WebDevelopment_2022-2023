from django.db.models import Avg
from datetime import datetime
from django.db.models import Count
from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):

    api_url = models.CharField(
        max_length=100, default="https://airlabs.co/api/v9/airports?", blank=True)
    api_key = models.CharField(
        max_length=100, default="4a84701d-216b-4db5-a5f6-5b69f85fe6d7", blank=True)


class FlightUser(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=15)

    def get_random_ticket_number(self):
        return User.objects.make_random_password(length=12, allowed_chars='1234567890')

    def __str__(self):
        return f"{self.ticket_number} ({self.user})"

    class Meta:
        verbose_name = "Flight Ticket"
        verbose_name_plural = "Flight Tickets"


class Flight(models.Model):
    FLIGHT_TYPES = (
        ('Departure', 'Departure'),
        ('Arrival', 'Arrival'),
    )

    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    flight_type = models.CharField(
        max_length=20, choices=FLIGHT_TYPES, default='Departure')

    gate = models.CharField(max_length=20)
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=10)

    # iata_codes
    source_airport_code = models.CharField(max_length=10)
    destination_airport_code = models.CharField(max_length=10)

    max_reservations = models.IntegerField(default=120)
    reservators = models.ManyToManyField(
        'User', through="FlightUser", blank=True)

    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )

    def get_reviews(self):
        return self.review_set.all()

    def get_user_review(self, user):
        return self.review_set.filter(user=user).first()

    def get_avg_rating(self):
        reviews = self.get_reviews()
        return reviews.aggregate(Avg("rating"))["rating__avg"] or 0

    def get_iata_code(self):
        """ Returns the list of two iata codes used in source_airport_code and destination_airport_code fields """
        return [self.source_airport_code, self.destination_airport_code]

    @classmethod
    def get_iata_codes(cls):
        """ Returns the list of all iata codes used in model """
        flights = cls.objects.all()
        iata_codes = []

        for flight in flights:
            iata_codes = [*iata_codes, *flight.get_iata_code()]

        return iata_codes

    @classmethod
    def group_by_day(cls, **kwargs):
        flights = cls.objects.filter(**kwargs)

        dates = flights.extra(
            select={'day': 'date( departure )'}
        ).values('day').annotate(available=Count('departure'))
        dates_dict = {}
        for date in dates:
            grouped_date = datetime.strptime(date['day'], '%Y-%m-%d').date()
            dates_dict[date['day']] = flights.filter(
                departure__contains=grouped_date)

        return dates_dict

    def __str__(self):
        return self.airline + " " + self.flight_number

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(
                arrival__gt=models.F('departure')), name='departure_arrival_check', violation_error_message='Departure must be earlier than arrival.'),
        ]


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.title
