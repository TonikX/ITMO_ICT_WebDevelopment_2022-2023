from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *


def main_page(request):
    return render(request, 'main_page.html', context={'rooms': Room.objects.all()})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main_page")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Вы успешно авторизовались в аккаунте {username}.")
                return redirect("main_page")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Вы успешно вышли из аккаунта")
    return redirect("main_page")


def room(request, pk):
    if request.method == "POST" and 'start_date' in request.POST:
        user_pk = request.user.pk
        booking_start_date = request.POST['start_date']
        booking_end_date = request.POST['end_date']
        booking_room_pk = request.POST['room_pk']
        guest = Guest.objects.get(pk=user_pk)
        room_obj = Room.objects.get(pk=booking_room_pk)
        new_booking = Booking(guest=guest, room=room_obj, checkin_date=booking_start_date, checkout_date=booking_end_date)
        new_booking.save()
        messages.info(request, f"Номер успешно забронирован с {booking_start_date} по {booking_end_date}")

    elif request.method == "POST" and 'comment_text' in request.POST:
        if request.user.is_anonymous:
            messages.warning(request, f"Оставлять комментарии могут только авторизованные пользователи")
        elif request.user.is_authenticated:
            user_pk = request.user.pk
            comment_text = request.POST['comment_text']
            rating = request.POST['rating']
            booking_room_pk = request.POST['room_pk']
            room_obj = Room.objects.get(pk=booking_room_pk)
            guest = Guest.objects.get(pk=user_pk)
            new_comment = Comment(text=comment_text, rating=rating, author=guest, room=room_obj)
            new_comment.save()
            messages.info(request, f"Комментарий успешно добавлен")

    room_obj = Room.objects.get(pk=pk)
    comments_obj = Comment.objects.filter(room=room_obj)
    return render(request, 'room_page.html', context={'room_obj': room_obj, 'comments': comments_obj})


def guests_table(request):
    last_month = datetime.today() - timedelta(days=30)
    last_month_bookings = Booking.objects.filter(checkin_date__gte=last_month)
    return render(request, 'guests_table.html', context={'bookings': last_month_bookings})


def my_booking(request):
    mybookings = Booking.objects.filter(guest=request.user.pk)
    return render(request, 'my_booking.html', context={'bookings': mybookings})


def delete_my_booking(request, pk):
    messages.success(request, "Ваша бронь успешно удалена")
    Booking.objects.filter(pk=pk).delete()
    return redirect('mybooking')


def edit_my_booking(request, pk):
    if request.method == "POST":
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        Booking.objects.filter(pk=pk).update(checkin_date=start_date, checkout_date=end_date)
        messages.info(request, f"Данные брони успешно изменены")
        return redirect('mybooking')
    else:
        booking = Booking.objects.get(pk=pk)
        return render(request, 'edit_booking.html', context={'booking': booking})
