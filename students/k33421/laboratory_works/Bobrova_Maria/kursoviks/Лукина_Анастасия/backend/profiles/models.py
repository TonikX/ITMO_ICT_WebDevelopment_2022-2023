from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone
from PIL import Image
import os


def get_path_upload_avatar(instance,file):
    """
    make path of uploaded file shorter and return it
    in following format: (media)/profile_pics/user_1/myphoto_2018-12-2.png
    """
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[-1]
    head = file.split('.')[0]
    if len(head) >10:
        head = head[:10]
    file_name =  head + '_' + time + '.' + end_extention
    return os.path.join('profile_pics','user_{0},{1}').format(instance.user.id,file_name)


class Profile(models.Model):
    """Модель профиля пользователя"""

    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    nike = models.CharField("НикНейм", max_length=100, null=True, blank=True)
    avatar = models.ImageField("Аватар", upload_to="profile/", null=True, blank=True)
    follow = models.ManyToManyField(User, verbose_name="Подписчики", related_name="follow_user")
    name = models.CharField(max_length=100, default="default")
    surname = models.CharField(max_length=100, default="default")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return "{}".format(self.user)

    @property
    def get_avatar_url(self):
        if self.avatar:
            return '/media/{}'.format(self.avatar)
        else:
            return '/static/img/default.png'

    @property
    def get_followers(self):
        if self.follow:
            return self.follow.all()
        else:
            return 'no followers yet'

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            print("avatar detected")
            img = Image.open(self.avatar.path)
            if img.height > 150 or img.width > 150:
                output_size = (150,150)
                img.thumbnail(output_size)
                img.save(self.avatar.path)    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля пользователя при регистрации"""
    if created:
        Profile.objects.create(user=instance, id=instance.id)
        # instance.profile.save()
