# Generated by Django 2.2.12 on 2023-05-23 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight_booking', '0003_auto_20230523_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=50)),
                ('passenger_email', models.EmailField(max_length=254)),
                ('seat_number', models.IntegerField()),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking.Flight')),
            ],
        ),
    ]
