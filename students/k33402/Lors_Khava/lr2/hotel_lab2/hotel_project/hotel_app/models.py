from django.db import models



class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Hotel(models.Model):
    clients = models.ManyToManyField(Client, through='Booking', related_name='clients')
    hotel_name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    address = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.hotel_name

class Room(models.Model):
    number = models.CharField(max_length=5)
    type = models.CharField(max_length=30, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, related_name='hotel_room')
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.number}"


class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='book_client')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='book_hotel')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='book_room')
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"{self.client}: {self.check_in_date} - {self.check_out_date}"


class Comment(models.Model):
    author = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name='author')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, related_name='inf_author')
    rating = models.IntegerField(choices=[(i, i) for i in range(0, 11)])
    review_comment = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.author}: {self.rating}"

