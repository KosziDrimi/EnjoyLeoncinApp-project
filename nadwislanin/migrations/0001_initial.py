# Generated by Django 3.2.8 on 2021-10-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.CharField(max_length=20)),
                ('numbers', models.CharField(max_length=20)),
                ('feedback', models.TextField()),
                ('new', models.BooleanField()),
                ('confirmation', models.TextField()),
                ('email_text', models.TextField()),
            ],
        ),
    ]
