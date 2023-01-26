### Create a new user
The interface allows to specify various fields such as first name, last name, etc.

To create a new user (reader), got to `/readers/create`. 


### Authorization
Users are authorized by their usernames and password. 
They can also be identified by an authentification token. 

To get one, go to `/auth/token/login`.


### Edit user data

You will be able to fill in the fields that have previously been empty or change the values of previously filled ones.

To update user information a user, go to `/auth/users/me`. 