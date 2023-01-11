from django.db import models

class Transport_owner(models.Model):
    id_owner = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    date_birthday = models.DateField()


class Transport(models.Model):
    id_car = models.IntegerField(primary_key=True)
    gov_number = models.CharField(max_length=15, null=False)
    marka = models.CharField(max_length=20, null=False)
    model_car = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    id_owner_car = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(Transport_owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Transport, on_delete=models.CASCADE)
    date_start = models.DateField()
    sate_end = models.DateField(null=True)


class Driver_doc(models.Model):
    id_doc = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(Transport_owner, on_delete=models.CASCADE, related_name="docs")
    number_doc = models.CharField(max_length=10, null=False)
    type_doc = models.CharField(max_length=10, null=False)
    date_start_doc = models.DateField()
