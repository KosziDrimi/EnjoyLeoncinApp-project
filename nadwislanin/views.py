from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from datetime import datetime

from .forms import ReservationForm, DetailsForm
from .models import Reservation
from core.settings import EMAIL_HOST_USER


def index(request):
    return render(request, 'nadwislanin/index.html')


@login_required
def reserve(request, tour=0):
    tour_number = tour
    form = ReservationForm(request.POST or None, initial={'tour': tour_number})

    if form.is_valid():
        res_email = form.cleaned_data['email']
        res_datetime = form.cleaned_data['datetime']
        res_tour = form.cleaned_data['tour']
        res_feedback = form.cleaned_data['feedback']

        res = Reservation(user=request.user, email=res_email, datetime=res_datetime, tour=res_tour,
                          feedback=res_feedback)
        res.save()

        context = {'name': request.user, 'datetime': res_datetime, 'email': res_email}
        return render(request, 'nadwislanin/thankyou.html', context)

    context = {'form': form}
    return render(request, 'nadwislanin/reservation.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required
def guest_page(request):
    reservations = Reservation.objects.filter(user=request.user)
    context = {'reservations': reservations}
    return render(request, 'nadwislanin/guest_page.html', context)


@login_required
def send_email(request, pk, nr):
    res = Reservation.objects.get(id=pk)

    if nr == 1:
        send_mail('Zapytanie - rejs Nadwiślaninem', res.email_text_one,
                  EMAIL_HOST_USER, [res.email], fail_silently=False)
        res.new = False

    elif nr == 2:
        send_mail('Potwierdzenie rejsu Nadwiślaninem', res.email_text_two,
                  EMAIL_HOST_USER, [res.email], fail_silently=False)
        res.confirmation = True

    res.save()
    messages.warning(request, 'Wiadomość została wysłana!')
    return redirect('update', res.id)


@login_required
def list_all(request, opt=all):
    option = opt

    if request.user.is_superuser:
        reservations = Reservation.objects.filter(datetime__gte=datetime.now())
        if option == 'new':
            reservations = Reservation.objects.filter(datetime__gte=datetime.now(), new=True, confirmation=False)
        elif option == 'old':
            reservations = Reservation.objects.filter(datetime__gte=datetime.now(), new=False, confirmation=False)
        elif option == 'cf':
            reservations = Reservation.objects.filter(datetime__gte=datetime.now(), new=False, confirmation=True)
        elif option == 'past':
            reservations = Reservation.objects.filter(datetime__lt=datetime.now())

        context = {'reservations': reservations}
        return render(request, 'nadwislanin/list_all.html', context)

    else:
        return HttpResponse('<h3>Nie masz uprawnień, aby wejść na tę stronę!</h3>')


@login_required
def update(request, pk):
    res = Reservation.objects.get(id=pk)
    form = DetailsForm(instance=res)

    if request.method == 'POST':
        form = DetailsForm(request.POST, instance=res)

        if form.is_valid():
            form.save()

            return redirect('update', res.id)

    context = {'form': form, 'res': res}
    return render(request, 'nadwislanin/details.html', context)


@login_required
def delete(request, pk):
    res = Reservation.objects.get(id=pk)
    res.delete()
    return redirect('list')


def tours(request):
    return render(request, 'nadwislanin/tours.html')


def info(request):
    return render(request, 'nadwislanin/info.html')


def rules(request):
    return render(request, 'nadwislanin/rules.html')


def rodo(request):
    return render(request, 'nadwislanin/rodo.html')


def gallery(request):
    return render(request, 'nadwislanin/gallery.html')
