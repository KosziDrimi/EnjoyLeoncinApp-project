# Generated by Django 3.2.8 on 2021-10-15 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nadwislanin', '0005_guest_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='name',
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]