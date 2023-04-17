# serializers.py
Describes serializers used to form views.

## Serializers:
* `PlaneSerializer`, `EmployeeSerializer` - Are used for create, update and delete operations, for redefinition fields in `FullFlightSerializer`.
* `TransitLandingSerializer` - Is used for create operations and for redefinition fields in `FullFlightSerializer`.
* `FlightSerializer` - Are used for create, update and delete operations.
* `FlightShortSerializer` - Is used for redefinition fields in `FullEmployeeSerializer` and `FullPlaneSerializer`.
* `FullFlightSerializer` - Is used for creation of full view of flight.
* `FullEmployeeSerializer` - Is used for creation of full view of employee.
* `FullPlaneSerializer` - Is used for creation of full view of plane.