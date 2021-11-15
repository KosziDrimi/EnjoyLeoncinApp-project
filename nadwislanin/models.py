from django.db import models
from django.contrib.auth.models import User


tour_choices = [('1', 'Mochty-smok tajemnice i legendy'),
                ('2', 'Ruiny spichlerza widziane z Narwi'),
                ('3', 'Kierunek Leoncin na styku trzech kultur')]


text_one = 'Dziękujemy za zainteresowanie rezerwacją rejsu Nadwiślaninem. \n' \
        'Potwierdzamy możliwość jego zorganizowania w dniu ... o godzinie ... . \n' \
        'Prosimy o dokonanie wpłaty na podany numer konta: 63 8011 0008 0040 0409 6821 0001. \n' \
        'Jesteśmy do dyspozycji w przypadku dodatkowych pytań. \nPozdrawiamy serdecznie, \nzałoga Nadwiślanina'

text_two = 'Dziękujemy za dokonanie wpłaty za rejs Nadwiślaninem. \nPotwierdzamy rezerwację w terminie ... . \n' \
         'Prosimy o przybycie 15 minut przed potwierdzoną godziną rejsu. \n' \
         'W systemie rezerwacyjnym po zalogowaniu istnieje możliwość sprawdzenia jego szczegółów. \n' \
         'Do zobaczenia w „Modlin Plaża”! \nPozdrawiamy, \nzałoga Nadwiślanina'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Nazwa użytkownika")
    email = models.EmailField(verbose_name="Adres e-mail")
    datetime = models.DateTimeField(verbose_name="Preferowana data i godzina rejsu")
    tour = models.CharField(max_length=2, choices=tour_choices, verbose_name="Wybrana wycieczka")
    feedback = models.TextField(verbose_name="Informacje dodatkowe", blank=True)
    new = models.BooleanField(default=True, verbose_name="Nowe zapytanie")
    confirmation = models.BooleanField(default=False, verbose_name="Potwierdzenie")
    email_text_one = models.TextField(default=text_one, verbose_name="Wiadomość e-mail I")
    email_text_two = models.TextField(default=text_two, verbose_name="Wiadomość e-mail II")

    def __str__(self):
        return f"""Rezerwacja ID {self.id}: {self.user} -> {self.datetime}"""
