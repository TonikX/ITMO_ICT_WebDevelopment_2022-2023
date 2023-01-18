from django.db import models


class RoomType(models.Model):
    id = models.AutoField("id", primary_key=True)
    pricePerNight = models.FloatField()
    name = models.TextField()



class Room(models.Model):
    id = models.AutoField("id", primary_key=True)
    roomType = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    number = models.IntegerField()
    isBooked = models.BooleanField()
    isCleaned = models.BooleanField()

class Client(models.Model):
    passport = models.CharField(max_length=20, primary_key=True)
    firstName = models.TextField()
    lastName = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    homeTown = models.TextField()

class Employee(models.Model):
    id = models.AutoField("id", primary_key=True)
    firstName = models.TextField()
    lastName = models.TextField()

class Cleening(models.Model):
    id = models.AutoField("id", primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    day = models.DateField()

class Booking(models.Model):
    bookStatusType = (
            ("F", "free"),
            ("B", "booked"),
        )

    paymentStatusType= (
        ("P", "payed"),
        ("N", "not payed"),
    )
    id = models.AutoField("id", primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    checkInDate = models.DateField()
    checkOutDate = models.DateField()
    bookStatus = models.CharField(choices=bookStatusType,max_length=20)
    paymentStatus = models.CharField(choices=paymentStatusType, max_length=20)



