import datetime
from typing import Optional

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import TemplateView

from rooms_app.forms import ReserveForm, AddComment, DeleteReserveForm, MoveReserveForm
from rooms_app.models import Hotel, Room, Reservation, Comment


class HotelsList(TemplateView):
    template_name = "hotels.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(hotels=Hotel.objects.all(), **kwargs)


class HotelView(TemplateView):
    template_name = "hotel.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(rooms=Room.objects.filter(hotel_id=kwargs["id"]),
                                        hotel=Hotel.objects.get(id=kwargs["id"]),
                                        reservations=Reservation.objects.filter(room__hotel_id=kwargs["id"],
                                                                                end_at__gt=datetime.datetime.now() - datetime.timedelta(
                                                                                    days=30),
                                                                                start_at__lt=datetime.datetime.now()),
                                        **kwargs)


class RoomDetails(TemplateView):
    template_name = "room_details.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(form=ReserveForm(), room=Room.objects.get(id=kwargs["id"]), **kwargs)

    def post(self, request: HttpRequest, **kwargs):
        form_data = ReserveForm(request.POST)
        if not form_data.is_valid():
            raise ValidationError("")
        start_at = form_data.cleaned_data["start_at"]
        end_at = form_data.cleaned_data["end_at"]
        user: Optional[AbstractUser] = request.user
        if user != None and user.is_authenticated:
            res = Reservation(user_id=user.pk, room_id=kwargs["id"], start_at=start_at, end_at=end_at)
            res.save()
        return redirect("/reservations/")


class ReservationsDetails(TemplateView):
    template_name = "reservations.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(form=None,
                                        reservations=Reservation.objects.filter(user_id=self.request.user.id), **kwargs)


class ReservationDetails(TemplateView):
    template_name = "reservation.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(comment_form=AddComment(prefix='comment'),
                                        delete_form=DeleteReserveForm(prefix='delete'),
                                        move_form=MoveReserveForm(prefix='move'),
                                        reservation=Reservation.objects.get(id=kwargs["id"]),
                                        comments=Comment.objects.filter(reservation_id=kwargs["id"]), **kwargs)

    def post(self, request: HttpRequest, **kwargs):
        move = MoveReserveForm(request.POST, prefix='move')
        if move.is_valid():
            reservation = Reservation.objects.get(id=kwargs["id"])
            reservation.start_at = move.cleaned_data["start_at"]
            reservation.end_at = move.cleaned_data["end_at"]
            reservation.save()
            return redirect("/reservations/")
        else:
            comment = AddComment(request.POST, prefix='comment')
            if comment.is_valid():
                comment = Comment(reservation_id=kwargs["id"], text=comment.cleaned_data["comment"],
                                  rate=comment.cleaned_data["rate"])
                comment.save()
                return redirect("/reservations/")
            else:
                delete = DeleteReserveForm(request.POST, prefix='delete')
                if delete.is_valid() and delete.cleaned_data["is_delete"]:
                    Reservation.objects.get(id=kwargs["id"]).delete()
                    return redirect("/reservations/")
                else:
                    raise ValidationError("")
