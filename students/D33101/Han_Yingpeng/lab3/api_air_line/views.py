from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate


from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import (
    User_serializer,Airline_serializer,Passenger_serializer,Review_serializer,Air_travel_serializer,CustomTokenObtainPairSerializer,user_token
)

from django.contrib.auth.models import User



# This code defines a class called "Login" that inherits from "TokenObtainPairView". 
# The class sets the serializer class to "CustomTokenObtainPairSerializer".

# The class has a post method that takes in a request object, along with other optional 
# arguments. The method retrieves the values of the 'username' and 'password' fields from 
# the request data. It then uses the authenticate method to check if the provided credentials 
# match a user in the system.

# If a user is found, the method proceeds to check if the user is active. If the user is active,
# the method creates an instance of the serializer class and checks if the data is valid. If the 
# data is valid, it calls a function called "user_token" to get user related data and return a 
# Response object containing a token, refresh token, user data and a message of successful login. 
# If the user is not active, the method return a response containing an error message 'user not active'
# with a status code of 400. If the credentials are invalid or no user is found, the method returns a 
# response containing an error message 'wrong username or password' with a status code of 400.

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if user.is_active:
                if login_serializer.is_valid():
                    user_serializer = user_token(user)
                    
                    return Response({
                        'token': login_serializer.validated_data.get('access'),
                        'refresh-token': login_serializer.validated_data.get('refresh'),
                        'user': user_serializer.data,
                        'message': 'Successful Login'
                    }, status=status.HTTP_200_OK)
                return Response({'error': 'wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'user not active'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)

# This code defines a class called "Logout" that inherits from "GenericAPIView".

# The class has a post method that takes in a request object, along with other optional arguments. 
# The method retrieves the value of the 'user' field from the request data and uses it to filter 
# the User model. If a user is found, it calls the "for_user" method on the "RefreshToken" class to 
# log out the user, and returns a response with a message 'logged out successfully' and a status code 
# of 200. If no user is found, the method returns a response with an error message 'user does not exist' 
# and a status code of 400.

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'logged out successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)


# The Airline_viewsets, Passenger_viewsets, Review_viewsets, User_viewsets, 
# and Air_travel_viewsets classes are all viewsets that inherit from Django 
# Rest Framework's ModelViewSet. They handle CRUD operations for their 
# respective models (Airline, Passenger, Review, User, and Air_travel) and 
# use serializers (Airline_serializer, Passenger_serializer, Review_serializer, 
# User_serializer, and Air_travel_serializer) to handle the data conversion between 
# the model and JSON. They also set the permission class to IsAuthenticated, meaning 
# that only authenticated user can access these viewsets.


class Airline_viewsets (viewsets.ModelViewSet):
    serializer_class = Airline_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Airline_serializer.Meta.model.objects.all()

     # The create method is used to handle the creation of a new Team instance. 
    # It takes the request data, converts it to a serializer, validates the data, 
    # and saves it to the database. If successful, it returns the newly created Team 
    # data along with a status of 201 (CREATED).

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # The destroy method is used to handle the deletion of a Team instance. 
    # It takes the primary key of the instance to be deleted, fetches the 
    # instance from the database, and deletes it. If successful, it returns 
    # a status of 204 (NO CONTENT).

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # The list method is used to handle the retrieval of a list of all Team 
    # instances. It takes the queryset, applies any filters specified in the 
    # request, paginates the data if necessary, and returns the list of Teams.


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # The update method is used to handle the updating of a Team instance

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # The partial_update method is used to handle partially updating a Team instance. 
    # It sets the partial argument to True and calls the update method with the provided arguments.
    # This allows for fields to be updated without having to provide all fields in the request.

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # The retrieve method is used to handle the retrieval of a specific Team instance.
    # It takes the primary key of the instance to be retrieved, fetches the instance 
    # from the database, converts it to a serializer, and returns the data of the Team instance.

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)   

class Passenger_viewsets (viewsets.ModelViewSet):
    serializer_class = Passenger_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Passenger_serializer.Meta.model.objects.all()  

     # The create method is used to handle the creation of a new Team instance. 
    # It takes the request data, converts it to a serializer, validates the data, 
    # and saves it to the database. If successful, it returns the newly created Team 
    # data along with a status of 201 (CREATED).

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # The destroy method is used to handle the deletion of a Team instance. 
    # It takes the primary key of the instance to be deleted, fetches the 
    # instance from the database, and deletes it. If successful, it returns 
    # a status of 204 (NO CONTENT).

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # The list method is used to handle the retrieval of a list of all Team 
    # instances. It takes the queryset, applies any filters specified in the 
    # request, paginates the data if necessary, and returns the list of Teams.


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # The update method is used to handle the updating of a Team instance

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # The partial_update method is used to handle partially updating a Team instance. 
    # It sets the partial argument to True and calls the update method with the provided arguments.
    # This allows for fields to be updated without having to provide all fields in the request.

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # The retrieve method is used to handle the retrieval of a specific Team instance.
    # It takes the primary key of the instance to be retrieved, fetches the instance 
    # from the database, converts it to a serializer, and returns the data of the Team instance.

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data) 

class Review_viewsets (viewsets.ModelViewSet):
    serializer_class = Review_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Review_serializer.Meta.model.objects.all()  

     # The create method is used to handle the creation of a new Team instance. 
    # It takes the request data, converts it to a serializer, validates the data, 
    # and saves it to the database. If successful, it returns the newly created Team 
    # data along with a status of 201 (CREATED).

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # The destroy method is used to handle the deletion of a Team instance. 
    # It takes the primary key of the instance to be deleted, fetches the 
    # instance from the database, and deletes it. If successful, it returns 
    # a status of 204 (NO CONTENT).

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # The list method is used to handle the retrieval of a list of all Team 
    # instances. It takes the queryset, applies any filters specified in the 
    # request, paginates the data if necessary, and returns the list of Teams.


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # The update method is used to handle the updating of a Team instance

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # The partial_update method is used to handle partially updating a Team instance. 
    # It sets the partial argument to True and calls the update method with the provided arguments.
    # This allows for fields to be updated without having to provide all fields in the request.

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # The retrieve method is used to handle the retrieval of a specific Team instance.
    # It takes the primary key of the instance to be retrieved, fetches the instance 
    # from the database, converts it to a serializer, and returns the data of the Team instance.

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data) 

class User_viewsets (viewsets.ModelViewSet):
    serializer_class = User_serializer
    permission_classes = (IsAuthenticated,)
    queryset = User_serializer.Meta.model.objects.all()  

     # The create method is used to handle the creation of a new Team instance. 
    # It takes the request data, converts it to a serializer, validates the data, 
    # and saves it to the database. If successful, it returns the newly created Team 
    # data along with a status of 201 (CREATED).

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # The destroy method is used to handle the deletion of a Team instance. 
    # It takes the primary key of the instance to be deleted, fetches the 
    # instance from the database, and deletes it. If successful, it returns 
    # a status of 204 (NO CONTENT).

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # The list method is used to handle the retrieval of a list of all Team 
    # instances. It takes the queryset, applies any filters specified in the 
    # request, paginates the data if necessary, and returns the list of Teams.


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # The update method is used to handle the updating of a Team instance

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # The partial_update method is used to handle partially updating a Team instance. 
    # It sets the partial argument to True and calls the update method with the provided arguments.
    # This allows for fields to be updated without having to provide all fields in the request.

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # The retrieve method is used to handle the retrieval of a specific Team instance.
    # It takes the primary key of the instance to be retrieved, fetches the instance 
    # from the database, converts it to a serializer, and returns the data of the Team instance.

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data) 

class Air_travel_viewsets (viewsets.ModelViewSet):
    serializer_class = Air_travel_serializer
    permission_classes = (IsAuthenticated,)
    queryset = Air_travel_serializer.Meta.model.objects.all()  

     # The create method is used to handle the creation of a new Team instance. 
    # It takes the request data, converts it to a serializer, validates the data, 
    # and saves it to the database. If successful, it returns the newly created Team 
    # data along with a status of 201 (CREATED).

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # The destroy method is used to handle the deletion of a Team instance. 
    # It takes the primary key of the instance to be deleted, fetches the 
    # instance from the database, and deletes it. If successful, it returns 
    # a status of 204 (NO CONTENT).

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # The list method is used to handle the retrieval of a list of all Team 
    # instances. It takes the queryset, applies any filters specified in the 
    # request, paginates the data if necessary, and returns the list of Teams.


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # The update method is used to handle the updating of a Team instance

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # The partial_update method is used to handle partially updating a Team instance. 
    # It sets the partial argument to True and calls the update method with the provided arguments.
    # This allows for fields to be updated without having to provide all fields in the request.

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # The retrieve method is used to handle the retrieval of a specific Team instance.
    # It takes the primary key of the instance to be retrieved, fetches the instance 
    # from the database, converts it to a serializer, and returns the data of the Team instance.

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data) 