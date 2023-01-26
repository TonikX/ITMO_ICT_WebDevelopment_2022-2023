from django.db import models

# Create your models here.

class Room(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    ROOM_TYPE = (
        ('1', '1 bed'),
        ('2', '2 beds'),
        ('3', '3 beds'))
    type = models.CharField(max_length=1, choices=ROOM_TYPE)
    floor = models.IntegerField()
    price = models.IntegerField()
    cleaners = models.ManyToManyField('Staff', through='Cleaning')

    def __str__(self):
        return f'Room №{self.number}'

class Staff(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f'Staff {self.name} {self.surname}'


class Guest(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    passport_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'Guest {self.name} {self.surname}'


class Cleaning(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cleaning')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='cleaning')
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cleaning №{self.id} in room № {self.room.id} by {self.staff.name} {self.staff.surname} at {self.date_time}'


class Checkin(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    check_in_date = models.DateField(auto_now_add=True)
    check_out_date = models.DateField(auto_now_add=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f'Guest {self.guest.name} {self.guest.surname} lives in room № {self.room.id} from {self.check_in_date} till {self.check_out_date}'