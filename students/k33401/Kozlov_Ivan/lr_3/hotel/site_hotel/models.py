from django.db import models


class TypeRoom(models.Model):
    id_type = models.AutoField("id",primary_key=True)
    facilities = models.TextField("удобства")
    count_places_in_room = models.IntegerField("количество мест в номере",null=False)
    name_type = models.CharField("название типа",max_length=400, null=False)


class Room(models.Model):
    id_room = models.AutoField(primary_key=True)
    type = models.ForeignKey("TypeRoom",on_delete=models.CASCADE, verbose_name="тип комнаты")
    room_number = models.IntegerField("номер комнаты", null=False)


class PriceConstructor(models.Model):
    id_price = models.AutoField(primary_key=True)
    type = models.ForeignKey("TypeRoom",on_delete=models.CASCADE, verbose_name="тип комнаты")
    data_start = models.DateField("Дата начала", null=False)
    data_end = models.DateField("Дата конца", null=False)
    price = models.FloatField("цена", null=False)


class Workers(models.Model):
    table_number = models.IntegerField("табельный номер", primary_key=True, null=False)
    fio = models.CharField("ФИО", null=False, max_length=300)
    phone_worker = models.CharField("телефон сотрудника", max_length=13, null=False, unique=True)


class Client(models.Model):
    passport = models.CharField("паспорт", max_length=20, primary_key=True)
    phone_client = models.CharField("телефон клиента", max_length=13, null=False)
    email_client = models.CharField("почта клиента", max_length=300, null=False)
    name = models.CharField("имя", max_length=20, null=False)
    last_name = models.CharField("фамилия", max_length=20, null=False)
    father_name = models.CharField("отчество", max_length=20, null=True)
    address = models.CharField("адрес проживания", max_length=300, null=True)


class Book(models.Model):
    status_type = (
            ("C", "Свободно"),
            ("З", "Занято"),
        )

    status_payment= (
        ("О", "Оплачено"),
        ("Н", "Не оплачено"),
    )

    move_out = (
        ("не выселен", "не выселен"),
        ("выселен", "выселен"),
    )

    number_contract = models.CharField("номер договора", max_length=400, primary_key=True)
    room = models.ForeignKey("Room", on_delete=models.CASCADE, verbose_name="номер комнаты")
    identifier_worker = models.ForeignKey("Workers", on_delete=models.CASCADE, verbose_name="табельный номер сотрудника")
    passport_client = models.ForeignKey("Client", on_delete=models.CASCADE, verbose_name="пасспорт клиента")
    data_start_living = models.DateField("дата заезда", null=False)
    data_end_living = models.DateField("дата выезда", null=False)
    status_book = models.CharField("статус бронирования", choices=status_type, null=False, max_length=20)
    status_payment = models.CharField("статус оплаты", choices=status_payment, null=False, max_length=20)
    status_move = models.CharField("Выселение", choices=move_out, null=False, max_length=20)

