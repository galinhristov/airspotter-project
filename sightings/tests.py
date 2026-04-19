from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from aviation.models import Airline, Aircraft, Airport
from sightings.models import Sighting

UserModel = get_user_model()

class SightingViewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='owner',
            password='StrongPass123!',
        )

        self.other_user = UserModel.objects.create_user(
            username='other',
            password='StrongPass123!',
        )

        self.airline = Airline.objects.create(
            name='Bulgaria Air',
            icao_code='LZB',
            iata_code='FB',
            country='Bulgaria',
        )

        self.airport = Airport.objects.create(
            name='Sofia Airport',
            icao_code='LBSF',
            iata_code='SOF',
            city='Sofia',
            country='Bulgaria',
        )

        self.aircraft = Aircraft.objects.create(
            registration='LZ-ROM',
            manufacturer='Airbus',
            model='A220-300',
            aircraft_type='Passenger',
            airline=self.airline,
            year_built=2024,
        )

        self.sighting = Sighting.objects.create(
            title='Test Sighting',
            description='Test description',
            spotted_at=timezone.now(),
            owner=self.user,
            aircraft=self.aircraft,
            airport=self.airport,
            status=Sighting.StatusChoices.PUBLISHED,
            visibility=Sighting.VisibilityChoices.PUBLIC,
        )

    def test_sighting_list_returns_200(self):
        response = self.client.get(reverse('sighting-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sightings/sighting-list.html')

    def test_sighting_detail_returns_200_for_public_sighting(self):
        response = self.client.get(reverse('sighting-details', kwargs={'pk': self.sighting.pk}))
        self.assertEqual(response.status_code, 200)

    def test_sighting_requires_login(self):
        response = self.client.get(reverse('sighting-create'))
        self.assertEqual(response.status_code, 302)

    def test_logged_user_can_create_sighting(self):
        self.client.login(username='owner', password='StrongPass123!')

        response = self.client.post(reverse('sighting-create'), data={
            'title': 'New Sighting',
            'description': 'Created through test',
            'spotted_at': timezone.now().strftime('%Y-%m-%dT%H:%M'),
            'aircraft': self.aircraft.pk,
            'airport': self.airport.pk,
            'status': Sighting.StatusChoices.PUBLISHED,
            'visibility': Sighting.VisibilityChoices.PUBLIC,
            'tags': [],
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Sighting.objects.filter(title='New Sighting').exists())

    def test_owner_can_edit_own_sighting(self):
        self.client.login(username='owner', password='StrongPass123!')
        response = self.client.get(reverse('sighting-edit', kwargs={'pk': self.sighting.pk}))
        self.assertEqual(response.status_code, 200)

    def test_non_owner_cannot_edit_sighting(self):
        self.client.login(username='other', password='StrongPass123!')
        response = self.client.get(reverse('sighting-edit', kwargs={'pk': self.sighting.pk}))
        self.assertEqual(response.status_code, 403)


    def test_owner_can_delete_own_sighting(self):
        self.client.login(username='owner', password='StrongPass123!')
        response = self.client.post(reverse('sighting-delete', kwargs={'pk': self.sighting.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Sighting.objects.filter(pk=self.sighting.pk).exists())

    def test_non_owner_cannot_delete_sighting(self):
        self.client.login(username='other', password='StrongPass123!')
        response = self.client.post(reverse('sighting-delete', kwargs={'pk': self.sighting.pk}))
        self.assertEqual(response.status_code, 403)





























