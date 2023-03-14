from django.db import models


class Auto(models.Model):
    def __str__(self):
        return self.brand + " " + self.model

    state_num = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Owner(models.Model):
    def __str__(self):
        return self.last_name + " " + self.first_name

    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    birthdate = models.DateTimeField(null=True)


class Ownage(models.Model):
    def __str__(self):
        return self.auto_id.brand + ' ' + self.auto_id.model + ' is owned by ' + self.owner_id.last_name + ' ' + self.owner_id.first_name

    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    auto_id = models.ForeignKey(Auto, on_delete=models.CASCADE, null=True, blank=True)
    begin_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=True, blank=True)


class License(models.Model):
    def __str__(self):
        return 'License of: ' + self.owner_id.last_name + " " + self.owner_id.first_name

    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, null=False)
    license_num = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    issue_date = models.DateTimeField(null=False)
