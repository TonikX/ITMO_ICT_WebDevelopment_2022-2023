from django.db import models
from django.contrib.auth import get_user_model


class Photo(models.Model):
    photo_id = models.CharField(primary_key=True, max_length=100)
    photo_url = models.CharField(max_length=100)
    photo_image_url = models.CharField(max_length=100)
    photo_width = models.IntegerField()
    photo_height = models.IntegerField()
    photo_description = models.CharField(max_length=200)
    photographer_username = models.CharField(max_length=100)
    photographer_first_name = models.CharField(max_length=100)
    photographer_last_name = models.CharField(max_length=100)
    blur_hash = models.CharField(max_length=200)


class Conversion(models.Model):
    keyword = models.CharField(max_length=30)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Keyword(models.Model):
    keyword = models.CharField(max_length=30)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    ai_score = models.FloatField(null=True, blank=True)


class Color(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    hex = models.CharField(max_length=10)
    keyword = models.CharField(max_length=30)
    red = models.IntegerField(null=True, blank=True)
    blue = models.IntegerField(null=True, blank=True)
    green = models.IntegerField(null=True, blank=True)


class LikePhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('photo', 'user',)


class Collection(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class CollectionPhoto(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, related_name="photo", on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, related_name='photos', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('photo', 'collection',)
