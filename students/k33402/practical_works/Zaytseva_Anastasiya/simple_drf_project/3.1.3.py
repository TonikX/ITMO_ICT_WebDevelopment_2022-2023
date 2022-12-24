from project_first_app.models import *
from django.db.models import Min, Max, Count

DrivingLicense.objects.filter(date_of_issue=DrivingLicense.objects.values("date_of_issue").aggregate(Min("date_of_issue"))["date_of_issue__min"])

Ownership.objects.values("date_of_start").aggregate(Max("date_of_start"))["date_of_start__max"]

ownershipCount = CarOwner.objects.annotate(Count("owner_ownership"))
for owner in ownershipCount:
    print(owner.username, owner.owner_ownership__count)

Car.objects.values("brand").annotate(Count("brand"))

CarOwner.objects.order_by("owner_license__date_of_issue")