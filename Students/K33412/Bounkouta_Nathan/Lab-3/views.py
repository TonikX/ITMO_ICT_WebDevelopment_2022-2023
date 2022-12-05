from .serializer import *
from rest_framework import generics


# Create your views here.

# Client
class ClientListAPIView(generics.ListAPIView):

    serializer_class = ClientViewSerializer

    def get_queryset(self):
        queryset = Client.objects.all()
        params = self.request.query_params

        legal_entity = params.get('legal_entity', None)

        if legal_entity:
            queryset = queryset.filter(legal_entity=legal_entity)

        return queryset


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer


class ClientRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientViewSerializer


# ServicesPL
class ServicesPLListAPIView(generics.ListAPIView):
    serializer_class = ServicesPLWTypeViewSerializer

    def get_queryset(self):
        queryset = ServicesPL.objects.all()
        params = self.request.query_params

        service_type = params.get('service_type', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        return queryset


class ServicesPLCreateAPIView(generics.CreateAPIView):
    queryset = ServicesPL.objects.all()
    serializer_class = ServicesPLCreateSerializer


class ServicesPLRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicesPL.objects.all()
    serializer_class = ServicesPLViewSerializer


# MaterialsPL
class MaterialsPLListAPIView(generics.ListAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLViewSerializer


class MaterialsPLCreateAPIView(generics.CreateAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLCreateSerializer


class MaterialsPLRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLViewSerializer


# Request
class RequestListAPIView(generics.ListAPIView):
    serializer_class = RequestWStatusViewSerializer

    def get_queryset(self):
        queryset = Request.objects.all()
        params = self.request.query_params

        status = params.get('status', None)
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)
        legal_entity = params.get('legal_entity', None)

        if status:
            queryset = queryset.filter(status=status)

        if from_date:
            queryset = queryset.filter(req_date__gte=from_date)

        if to_date:
            queryset = queryset.filter(req_date__lte=to_date)

        if legal_entity:
            queryset = queryset.filter(client__legal_entity=legal_entity)

        return queryset


class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer


class RequestRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestViewSerializer


class RequestNestedAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestNestedSerializer


# ChosenServices
class ChosenServicesListAPIView(generics.ListAPIView):
    serializer_class = ChosenServicesWSRViewSerializer

    def get_queryset(self):
        queryset = ChosenServices.objects.all()
        params = self.request.query_params

        req = params.get('req', None)

        if req:
            queryset = queryset.filter(req=req)

        return queryset


class ChosenServicesCreateAPIView(generics.CreateAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesCreateSerializer


class ChosenServicesRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesViewSerializer


class ChosenServicesFullListAPIView(generics.ListAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesNestedSerializer


# ChosenMaterials
class ChosenMaterialsListAPIView(generics.ListAPIView):
    serializer_class = ChosenMaterialWMRsViewSerializer

    def get_queryset(self):
        queryset = ChosenMaterials.objects.all()
        params = self.request.query_params

        req = params.get('req', None)

        if req:
            queryset = queryset.filter(req=req)

        return queryset


class ChosenMaterialsCreateAPIView(generics.CreateAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsCreateSerializer


class ChosenMaterialsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsViewSerializer


class ChosenMaterialsFullListAPIView(generics.ListAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsNestedSerializer


# WorkGroup
class WorkGroupListAPIView(generics.ListAPIView):
    serializer_class = WorkGroupWREViewSerializer

    def get_queryset(self):
        queryset = WorkGroup.objects.all()
        params = self.request.query_params

        req = params.get('req', None)
        executor = params.get('executor', None)
        start_date = params.get('start_date', None)
        end_date = params.get('end_date', None)

        if req:
            queryset = queryset.filter(req=req)

        if executor:
            queryset = queryset.filter(executor=executor)

        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)

        if end_date:
            queryset = queryset.filter(end_date__lte=end_date)

        return queryset


class WorkGroupCreateAPIView(generics.CreateAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupCreateSerializer


class WorkGroupRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupViewSerializer


class WorkGroupFullListAPIView(generics.ListAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupNestedSerializer


# Executor
class ExecutorListAPIView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorViewSerializer


class ExecutorCreateAPIView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorCreateSerializer


class ExecutorRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorViewSerializer


# Invoice
class InvoiceListAPIView(generics.ListAPIView):
    serializer_class = InvoiceViewNestedSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        params = self.request.query_params

        legal_entity = params.get('legal_entity', None)

        if legal_entity:
            queryset = queryset.filter(client__legal_entity=legal_entity)

        return queryset


class InvoiceCreateAPIView(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceCreateSerializer


class InvoiceRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceViewSerializer


# PaymentOrder
class PaymentOrderListAPIView(generics.ListAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderNestedSerializer


class PaymentOrderCreateAPIView(generics.CreateAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderCreateSerializer


class PaymentOrderRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderViewSerializer