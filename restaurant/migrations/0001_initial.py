# Generated by Django 4.2.1 on 2023-05-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('no_of_guests', models.IntegerField(max_length=6)),
                ('BookingDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inventory', models.IntegerField(max_length=5)),
            ],
        ),
    ]
