from .models import *
from rest_framework import serializers


# Клиент

class ClientViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientCreateSerializer(serializers.Serializer):
    legal_entity = serializers.CharField(max_length=60)
    contact_person = serializers.CharField(max_length=60)
    phone_num = serializers.CharField(max_length=12)
    email = serializers.CharField(max_length=30)
    bank_details = serializers.CharField(max_length=30)

    def create(self, validated_data):
        client = Client(**validated_data)
        client.save()
        return Client(**validated_data)


# Прайс-лист на услуги

class ServicesPLViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesPL
        fields = "__all__"


class ServicesPLWTypeViewSerializer(serializers.ModelSerializer):
    service_type = serializers.CharField(source="get_service_type_display", read_only=True)

    class Meta:
        model = ServicesPL
        fields = "__all__"


class ServicesPLCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    price = serializers.CharField(max_length=30)
    service_type = serializers.ChoiceField(choices=ServicesPL.service_types)

    def create(self, validated_data):
        services_pl = ServicesPL(**validated_data)
        services_pl.save()
        return ServicesPL(**validated_data)


# Прайс-лист на материалы

class MaterialsPLViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialsPL
        fields = "__all__"


class MaterialsPLCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=150)
    price = serializers.CharField(max_length=30)

    def create(self, validated_data):
        materials_pl = MaterialsPL(**validated_data)
        materials_pl.save()
        return MaterialsPL(**validated_data)


# Заявка

class RequestViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"


class RequestWStatusViewSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Request
        fields = "__all__"


class RequestNestedSerializer(serializers.ModelSerializer):
    client = ClientViewSerializer()
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Request
        fields = "__all__"


class RequestCreateSerializer(serializers.Serializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    req_date = serializers.DateField()
    workload = serializers.CharField(max_length=30)
    final_price = serializers.CharField(max_length=30)
    status = serializers.ChoiceField(choices=Request.status_types)

    def create(self, validated_data):
        request = Request(**validated_data)
        request.save()
        return Request(**validated_data)


# Исполнитель

class ExecutorViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = "__all__"


class ExecutorCreateSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50)
    phone_num = serializers.CharField(max_length=12)

    def create(self, validated_data):
        executor = Executor(**validated_data)
        executor.save()
        return Executor(**validated_data)


# Заявка - Услуги

class ChosenServicesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenServices
        fields = "__all__"


class ChosenServicesWSRViewSerializer(serializers.ModelSerializer):
    service = serializers.StringRelatedField(read_only=True)
    req = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ChosenServices
        fields = "__all__"


class ChosenServicesCreateSerializer(serializers.Serializer):
    service = serializers.PrimaryKeyRelatedField(queryset=ServicesPL.objects.all())
    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())
    total_cost = serializers.CharField(max_length=30)

    def create(self, validated_data):
        chosen_services = ChosenServices(**validated_data)
        chosen_services.save()
        return ChosenServices(**validated_data)


class ChosenServicesNestedSerializer(serializers.ModelSerializer):
    req = RequestNestedSerializer()
    service = ServicesPLWTypeViewSerializer()

    class Meta:
        model = ChosenServices
        fields = "__all__"


# Заявка - Материалы

class ChosenMaterialsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenMaterials
        fields = "__all__"


class ChosenMaterialWMRsViewSerializer(serializers.ModelSerializer):
    material = serializers.StringRelatedField(read_only=True)
    req = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ChosenMaterials
        fields = "__all__"


class ChosenMaterialsCreateSerializer(serializers.Serializer):
    material = serializers.PrimaryKeyRelatedField(queryset=MaterialsPL.objects.all())
    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())

    total_cost = serializers.CharField(max_length=30)
    amount = serializers.IntegerField()

    def create(self, validated_data):
        chosen_materials = ChosenMaterials(**validated_data)
        chosen_materials.save()
        return ChosenMaterials(**validated_data)


class ChosenMaterialsNestedSerializer(serializers.ModelSerializer):
    req = RequestNestedSerializer()
    material = MaterialsPLViewSerializer()

    class Meta:
        model = ChosenMaterials
        fields = "__all__"


# Рабочая группа

class WorkGroupViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkGroup
        fields = "__all__"


class WorkGroupWREViewSerializer(serializers.ModelSerializer):
    req = serializers.StringRelatedField(read_only=True)
    executor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = WorkGroup
        fields = "__all__"


class WorkGroupCreateSerializer(serializers.Serializer):
    executor = serializers.PrimaryKeyRelatedField(queryset=Executor.objects.all())
    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())

    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self, validated_data):
        work_group = WorkGroup(**validated_data)
        work_group.save()
        return WorkGroup(**validated_data)


class WorkGroupNestedSerializer(serializers.ModelSerializer):
    req = RequestNestedSerializer()
    executor = ExecutorViewSerializer()

    class Meta:
        model = WorkGroup
        fields = "__all__"


# Счет на оплату

class InvoiceViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceViewNestedSerializer(serializers.ModelSerializer):
    req = RequestWStatusViewSerializer()
    client = ClientViewSerializer()

    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceCreateSerializer(serializers.Serializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())

    pay_due = serializers.DateField()

    def create(self, validated_data):
        invoice = Invoice(**validated_data)
        invoice.save()
        return Invoice(**validated_data)


# Платежное поручение
class PaymentOrderViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentOrder
        fields = "__all__"


class PaymentOrderNestedSerializer(serializers.ModelSerializer):
    req = RequestWStatusViewSerializer()
    client = ClientViewSerializer()
    invoice = InvoiceViewSerializer()

    class Meta:
        model = PaymentOrder
        fields = "__all__"


class PaymentOrderCreateSerializer(serializers.Serializer):
    req = serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())

    pay_date = serializers.DateField()

    def create(self, validated_data):
        payment_order = PaymentOrder(**validated_data)
        payment_order.save()
        return PaymentOrder(**validated_data)


class TestSerializer(serializers.ModelSerializer):  # изменить сериализаторы? добавить новые?

    requests_of_user = RequestWStatusViewSerializer(many=True)

    class Meta:
        model = Client
        fields = ['legal_entity', 'contact_person', 'phone_num', 'email', 'bank_details', 'requests_of_user']
