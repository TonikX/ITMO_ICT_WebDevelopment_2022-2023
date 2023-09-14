from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, exceptions, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from typography.auth import MCProfilesAuthentication, NonStrictManagerAuthentication, CustomerAuthentication
from typography.exceptions import BadRequest
from typography.models import Customer, Manager
from typography.serializers import PublicCustomerSerializer, PrivateAuthorSerializer, PrivateCustomerSerializer


class CustomerListCreatePermissions(permissions.BasePermission):
	def has_permission(self, request, view):
		return \
				request.method == "GET" and isinstance(request.auth, Manager) or \
				request.method == "POST" and request.user and request.user.is_authenticated


class CustomersApiView(generics.ListCreateAPIView):
	authentication_classes = [NonStrictManagerAuthentication]
	permission_classes = [CustomerListCreatePermissions]
	queryset = Customer.objects.all()
	serializer_class = PublicCustomerSerializer

	@swagger_auto_schema(
		responses={201: openapi.Response("Данные клиента", PublicCustomerSerializer),
		           400: "Unable to create another customer profile"}
	)
	def post(self, request):
		if self.get_queryset().filter(user=request.user).exists():
			raise BadRequest("Unable to create another customer profile")

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(user=request.user)
		return Response(serializer.data, status=201)


class CustomerSingleViewPermissions(permissions.BasePermission):
	def has_permission(self, request, view):
		return \
				request.method == "GET" and isinstance(request.auth, Manager) or \
				request.method == "POST" and request.user and request.user.is_authenticated


@swagger_auto_schema(
	method="GET",
	responses={
		200: openapi.Response("Данные клиента", PrivateAuthorSerializer),
		401: "You can only see full information about your own account"
	}
)
@api_view(["GET"])
@authentication_classes([MCProfilesAuthentication])
@permission_classes([IsAuthenticated])
def get_customer_full(request: Request, pk: int):
	customer = Customer.objects.get(user=pk)
	if isinstance(request.auth, Customer):
		current_customer: Customer = request.auth
		if current_customer != customer:
			raise exceptions.AuthenticationFailed("You can only see full information about your own account")

	serializer = PrivateCustomerSerializer(customer)
	return Response(serializer.data)


@swagger_auto_schema(
	method="GET",
	responses={
		200: openapi.Response("Данные клиента", PrivateAuthorSerializer),
	}
)
@api_view(["GET"])
@authentication_classes([CustomerAuthentication])
@permission_classes([IsAuthenticated])
def get_customer_full_me(request: Request):
	customer = Customer.objects.get(user=request.user)
	serializer = PrivateCustomerSerializer(customer)
	return Response(serializer.data)
