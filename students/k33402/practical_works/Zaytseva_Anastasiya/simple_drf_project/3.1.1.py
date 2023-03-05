from project_first_app.models import *

carOwners = []

carOwners.append(CarOwner.objects.create(username="owner1",last_name="Ivanov",first_name="Ivan",date_of_birth="1990-12-11",passport_number="4013888001",address="Saint Petersburg, ul. Pushkina, d. 1"))
carOwners.append(CarOwner.objects.create(username="owner2",last_name="Petrov",first_name="Petr",date_of_birth="1990-11-11",passport_number="4013888002",address="Saint Petersburg, ul. Pushkina, d. 2"))
carOwners.append(CarOwner.objects.create(username="owner3",last_name="Danilov",first_name="Danil",date_of_birth="1990-10-11",passport_number="4013888003",address="Saint Petersburg, ul. Pushkina, d. 3"))
carOwners.append(CarOwner.objects.create(username="owner4",last_name="Glebov",first_name="Gleb",date_of_birth="1990-09-11",passport_number="4013888004",address="Saint Petersburg, ul. Pushkina, d. 4"))
carOwners.append(CarOwner.objects.create(username="owner5",last_name="Sergeev",first_name="Sergei",date_of_birth="1990-08-11",passport_number="4013888005",address="Saint Petersburg, ul. Pushkina, d. 5"))
carOwners.append(CarOwner.objects.create(username="owner6",last_name="Maksimov",first_name="Maksimov",date_of_birth="1990-07-11",passport_number="4013888006",address="Saint Petersburg, ul. Pushkina, d. 6"))
carOwners.append(CarOwner.objects.create(username="owner7",last_name="Artemov",first_name="Artem",date_of_birth="1990-06-11",passport_number="4013888007",address="Saint Petersburg, ul. Pushkina, d. 7"))

for owner in carOwners:
    print(owner)

cars = []

cars.append(Car.objects.create(gov_number="A777AA",brand="Renault",model="Logan",color="grey"))
cars.append(Car.objects.create(gov_number="B777BB",brand="Renault",model="Duster",color="blue"))
cars.append(Car.objects.create(gov_number="C777CC",brand="Toyota",model="Camry",color="black"))
cars.append(Car.objects.create(gov_number="E777EE",brand="Wolksvagen",model="Polo",color="grey"))
cars.append(Car.objects.create(gov_number="H777HH",brand="Wolksvagen",model="Amarok",color="brown"))
cars.append(Car.objects.create(gov_number="K777KK",brand="Kia",model="Rio",color="red"))

for car in cars:
    print(car)

licenses = []

for owner in carOwners:
    licenses.append(DrivingLicense.objects.create(id_owner=owner,license_number="0001111101",type="B",date_of_issue="2013-08-08"))

for license in licenses:
    print(license)

Ownership.objects.create(id_owner=carOwners[0],id_car=cars[0],date_of_start="2008-01-01",date_of_end="2009-01-01")
Ownership.objects.create(id_owner=carOwners[0],id_car=cars[1],date_of_start="2009-01-01",date_of_end="2010-01-01")
Ownership.objects.create(id_owner=carOwners[0],id_car=cars[2],date_of_start="2010-01-01")

Ownership.objects.create(id_owner=carOwners[1],id_car=cars[3],date_of_start="2008-01-01",date_of_end="2009-01-01")
Ownership.objects.create(id_owner=carOwners[1],id_car=cars[4],date_of_start="2009-01-01")

Ownership.objects.create(id_owner=carOwners[2],id_car=cars[5],date_of_start="2008-01-01",date_of_end="2009-01-01")

Ownership.objects.create(id_owner=carOwners[3],id_car=cars[0],date_of_start="2009-01-01",date_of_end="2010-01-01")
Ownership.objects.create(id_owner=carOwners[3],id_car=cars[1],date_of_start="2010-01-01")

Ownership.objects.create(id_owner=carOwners[4],id_car=cars[3],date_of_start="2009-01-01")

Ownership.objects.create(id_owner=carOwners[5],id_car=cars[0],date_of_start="2010-01-01")

Ownership.objects.create(id_owner=carOwners[6],id_car=cars[0],date_of_start="2007-01-01",date_of_end="2008-01-01")
Ownership.objects.create(id_owner=carOwners[6],id_car=cars[1],date_of_start="2008-01-01",date_of_end="2009-01-01")
Ownership.objects.create(id_owner=carOwners[6],id_car=cars[5],date_of_start="2009-01-01")

for car in cars:
    print(car.owners.all())
