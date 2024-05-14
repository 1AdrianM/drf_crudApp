# Generated by Django 5.0.6 on 2024-05-14 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerId', models.IntegerField()),
                ('CustomerName', models.CharField(max_length=100)),
                ('RoomNumber', models.IntegerField()),
                ('CheckingDate', models.DateTimeField()),
                ('NumberOfcustomers', models.IntegerField()),
            ],
        ),
    ]