# Generated by Django 5.0.6 on 2024-05-14 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookingId', models.IntegerField()),
                ('CustomerName', models.CharField(max_length=100)),
                ('RoomNumber', models.IntegerField()),
                ('CheckingDate', models.DateTimeField()),
                ('CheckoutOrder', models.DateTimeField()),
                ('TotalPrice', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
