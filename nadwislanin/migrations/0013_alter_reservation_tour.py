# Generated by Django 3.2.8 on 2021-11-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nadwislanin', '0012_auto_20211115_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='tour',
            field=models.CharField(choices=[('1', 'Mochty-smok tajemnice i legendy'), ('2', 'Ruiny spichlerza widziane z Narwi'), ('3', 'Kierunek Leoncin na styku trzech kultur')], max_length=2, verbose_name='Wybrana wycieczka'),
        ),
    ]