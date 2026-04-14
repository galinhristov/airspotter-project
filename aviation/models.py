from django.core.exceptions import ValidationError
from django.db import models


def validate_airline_icao_code(value):
    if len(value) != 3:
        raise ValidationError('Airline ICAO code must be exactly 3 characters.')


def validate_airline_iata_code(value):
    if len(value) != 2:
        raise ValidationError('Airline IATA code must be exactly 2 characters.')


def validate_airport_icao_code(value):
    if len(value) != 4:
        raise ValidationError('Airport ICAO code must be exactly 4 characters.')


def validate_airport_iata_code(value):
    if len(value) != 3:
        raise ValidationError('Airport IATA code must be exactly 3 characters.')


#=====================================================
# Compatibility validators for old migration file only
def validate_icao_code(value):
    if len(value) != 4:
        raise ValidationError('Airport ICAO code must be exactly 4 characters.')


def validate_iata_code(value):
    if len(value) != 3:
        raise ValidationError('Airport IATA code must be exactly 3 characters.')



class Airline(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    icao_code = models.CharField(
        max_length=3,
        unique=True,
        validators=[validate_airline_icao_code],
    )
    iata_code = models.CharField(
        max_length=2,
        unique=True,
        validators=[validate_airline_iata_code],
    )
    country = models.CharField(
        max_length=60,
    )
    logo = models.ImageField(
        upload_to='airlines/',
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



class Airport(models.Model):
    name = models.CharField(
        max_length=120,
    )
    icao_code = models.CharField(
        max_length=4,
        unique=True,
        validators=[validate_airport_icao_code],
    )
    iata_code = models.CharField(
        max_length=3,
        unique=True,
        validators=[validate_airport_iata_code],
    )
    city = models.CharField(
        max_length=80,
    )
    country = models.CharField(
        max_length=60,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.iata_code})'


class Aircraft(models.Model):
    registration = models.CharField(
        max_length=20,
        unique=True,
    )
    manufacturer = models.CharField(
        max_length=60,
    )
    model = models.CharField(
        max_length=60,
    )
    aircraft_type = models.CharField(
        max_length=50,
    )
    airline = models.ForeignKey(
        Airline,
        on_delete=models.CASCADE,
        related_name='aircraft',
    )
    year_built = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
    )


    class Meta:
        ordering = ('registration',)

    def __str__(self):
        return f'{self.registration} - {self.manufacturer} {self.model}'
