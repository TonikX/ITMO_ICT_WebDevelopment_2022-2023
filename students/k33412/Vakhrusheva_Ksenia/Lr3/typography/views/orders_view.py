from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, exceptions, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from typography.auth import MCProfilesAuthentication
from typography.models import Manager, Order, Customer
from typography.serializers import OrderSerializer, CreateOrderSerializer, FullOrderSerializer


class OrdersApiViewPermissions(permissions.BasePermission):
	def has_permission(self, request, view):
		return \
				request.method == "GET" and isinstance(request.auth, Manager) or \
				request.method == "POST" and isinstance(request.auth, Customer)


class OrdersApiView(generics.ListCreateAPIView):
	authentication_classes = [MCProfilesAuthentication]
	permission_classes = [OrdersApiViewPermissions]
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	@swagger_auto_schema(
		request_body=CreateOrderSerializer,
		responses={201: openapi.Response("Данные созданного заказа", OrderSerializer)}
	)
	def post(self, request: Request):
		serializer = CreateOrderSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		new_order = serializer.save(customer=request.auth)
		return Response(OrderSerializer(new_order).data, status=201)


class OrderSingleViewPermissions(permissions.BasePermission):
	def has_permission(self, request, view):
		return \
				request.method == "GET" and request.user and request.user.is_authenticated or \
				request.method == "DELETE" and isinstance(request.auth, Manager)


class OrderSingleViewDeleteAPIView(APIView):
	authentication_classes = [MCProfilesAuthentication]
	permission_classes = [OrderSingleViewPermissions]

	@swagger_auto_schema(
		responses={200: openapi.Response("Данные заказа", FullOrderSerializer),
		           401: "You can only see full information about your orders"}
	)
	def get(self, request: Request, pk: int):
		order = Order.objects.get(id=pk)

		if isinstance(request.auth, Customer):
			current_customer: Customer = request.auth
			if current_customer != order.customer:
				raise exceptions.AuthenticationFailed("You can only see full information about your orders")

		serializer = FullOrderSerializer(order)
		return Response(serializer.data)

	@swagger_auto_schema(
		responses={204: "No content"}
	)
	def delete(self, request: Request, pk: int):
		order = Order.objects.get(id=pk)
		order.delete()
		return Response(status=204)
