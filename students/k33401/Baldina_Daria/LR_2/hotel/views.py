from django.shortcuts import render, redirect
from msilib.schema import ListView
from django.http import HttpResponseForbidden
from .models import Hotel, Reservation,Room, Comment
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


#главная страница
def main_page(request):
    return render(request, 'main_page.html')


#для реистрации гостей

def registerPage(requset):
    form = RegisterForm

    if requset.method == "POST":
        form = RegisterForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(requset, 'register_guests.html', context)

#вход в аккаунт

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/main/')

    context = {}

    return render(request, 'login.html', context)

#выход из аккаунта
class Logout(LogoutView):
    template_name='logout.html'


#просмотр всех номеров
class RoomsList(ListView):
    model = Room
    template_name = 'list_rooms.html'

#бронирование
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    fields = ['room', 'arrival_date', 'departure_date']
    template_name = 'create_reservation.html'
    success_url = '/users_bookings'

    def form_valid(self, form):
        form.instance.guest = self.request.user
        return super(BookingCreateView, self).form_valid(form)


#просмотр бронирований пользователя
def user_book(request):
    need_book = Reservation.objects.filter(guest=request.user) 
    current_book = {"object_list": need_book}
    return render(request, 'users_bookings.html', current_book)


#редактирование брони
class UpdateBooking(UpdateView):
    model = Reservation
    fields = ['room', 'arrival_date', 'departure_date']
    template_name = 'update_book.html'
    success_url = '/users_bookings/'

#удаление брони
class DeleteBooking(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'del_book.html'
    success_url = '/users_bookings/'

    def delete(self, request, *args, **kwargs):
        # Only allow the creator of booking to delete it
        if self.get_object().guest == request.user:
            return super(DeleteBooking, self).delete(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You can't cancel this booking")

#написать комментарий
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['reservation', 'text', 'rate']
    template_name = 'create_comment.html'
    success_url = '/all_comments/'

    def form_valid(self, form):
        form.instance.guest = User.objects.get(username = self.request.user.username)
        return super(CommentCreateView, self).form_valid(form)

#посмотреть все комментарии
def all_comments(request):
    list_comments = {"object_list": Comment.objects.all()}
    return render(request, 'all_comments.html', list_comments)

# #таблица гостей отелей
# def get_hotel(request):
#     hotel = request.POST.get('hotel_name')
#     if hotel:
#         return redirect(f"/guests/{hotel}")
#     else:
#         return render(request, 'hotel.html')

def guests_list(request):
    guest_in_hotel = Reservation.objects.all()
    list_of_guests = {
        "object_list": guest_in_hotel}
    return render(request, 'guests.html', list_of_guests)
