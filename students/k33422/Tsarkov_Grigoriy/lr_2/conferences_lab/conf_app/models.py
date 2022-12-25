from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings 


class Conference(models.Model):
    name = models.CharField("conference", max_length=50)
    topic = models.CharField("topic", blank=True, choices=[
        ("business", "business"),
        ("design", "design"),
        ("physics", "physics"),
    ], max_length=10)
    location = models.CharField("location", max_length=100)
    start_date = models.DateField("start date")
    end_date = models.DateField("end date")
    description = models.CharField("conference description", max_length=200)
    location_description = models.CharField("location description", max_length=200)
    terms = models.CharField("participation terms", max_length=1000)
    speaker = models.ManyToManyField(User, related_name="speaker")
    recommend = models.CharField("recommend", choices=[
        ("yes", "yes"),
        ("no", "no"),
    ], max_length=3)


    class Meta:
        verbose_name = "conference"
        verbose_name_plural = "conferences"

    def __str__(self):
        return f"{self.topic}: {self.name}"

    def written_by(self):
        return ", ".join([str(p) for p in self.speaker.all()])


class Comment(models.Model):
    name = models.ForeignKey(Conference, on_delete=models.CASCADE, verbose_name="conference")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="comment author")
    text = models.CharField("comment", max_length=100)
    rating = models.CharField("rating", choices =[
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),

    ], max_length=2)


    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.author}: {self.text}"
