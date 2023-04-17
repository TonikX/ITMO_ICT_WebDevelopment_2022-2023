# url.py
Describes urls for service usage.

## URLs:
* `flight/<number>/` - Shows the full info about this flight including the crew and transit landings. Instead of <number> is required an id of flight.
* `flights/` - Shows all the flights.
* `employee/<number>/` - Shows the full info about this employee including the flight numbers they have allowance to. Instead of <number> is required an id of employee.
* `employees/` - Shows all the employees.
* `plane/<number>/` - Shows the full info about this plane including the flight numbers it is used to. Instead of <number> is required an id of plane.
* `planes/` - Shows all the employees.
* `flight/create/` - Creates a new flight.
* `employee/create/` - Creates a new employee.
* `plane/create/` - Creates a new plane.
* `transit_land/create/` - Creates a new transit landing.
* `flight/upd_del/<number>/` - Updates or deletes a flight. Instead of <number> is required an id of flight.
* `employee/upd_del/<number>/` - Updates or deletes an employee. Instead of <number> is required an id of employee.
* `plane/upd_del/<number>/` - Updates or deletes a plane. Instead of <number> is required an id of plane.