# models.py

Describes the models that are used to create the service.

## Models:

* `Employee` - An employee of a company.
    * `position` - Position in the crew (commander, second pilot, navigator or steward)
    * `experience` - Number of years worked in this position.
* `Plane` - A plane of some flight with its characteristics.
* `TransitLanding` - A transit landing during the flight.
    * `dep_dt/arr_dt` - Departure/Arrival date and time.
* `Flight` - A flight served by a compony.
    * `air_departure/air_arrival` - An airport of departure/arrival.
    * `dep_dt/arr_dt` - Departure/Arrival date and time.
* `Allowance` - Employee's allowance to flight. 