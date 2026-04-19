from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from aviation.models import Airline, Airport, Aircraft
from community.models import Collection
from sightings.models import Sighting

UserModel = get_user_model()

class CollectionViewTest(TestCase):
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
        )

        self.sighting = Sighting.objects.create(
            title='Owned Sighting',
            description='Owned by test user',
            spotted_at=timezone.now(),
            owner=self.user,
            aircraft=self.aircraft,
            airport=self.airport,
            status=Sighting.StatusChoices.PUBLISHED,
            visibility=Sighting.VisibilityChoices.PUBLIC,
        )

        self.collection = Collection.objects.create(
            title='My Collection',
            description='Test Collection',
            owner=self.user,
            is_public=True,
        )
        self.collection.sightings.add(self.sighting)

    def test_collection_list_requires_login(self):
        response = self.client.get(reverse('collection-list'))
        self.assertEqual(response.status_code, 302)

    def test_owner_can_open_collection_list(self):
        self.client.login(username='owner', password='StrongPass123!')
        response = self.client.get(reverse('collection-list'))
        self.assertEqual(response.status_code, 200)

    def test_owner_can_open_collection_detail(self):
        self.client.login(username='owner', password="StrongPass123!")
        response = self.client.get(reverse('collection-details', kwargs={'pk': self.collection.pk}))
        self.assertEqual(response.status_code, 200)

    def test_non_owner_cannot_open_collection_detail(self):
        self.client.login(username='other', password='StrongPass123!')
        response = self.client.get(reverse('collection-details', kwargs={'pk': self.collection.pk}))
        self.assertEqual(response.status_code, 404)

    def test_owner_can_create_collection(self):
        self.client.login(username='owner', password='StrongPass123!')
        response = self.client.post(reverse('collection-create'), data={
            'title': 'Summer Spotting',
            'description': 'Best sightings',
            'sightings': [self.sighting.pk],
            'is_public': True,
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Collection.objects.filter(title='Summer Spotting').exists())

    def test_owner_can_delete_collection(self):
        self.client.login(username='owner', password='StrongPass123!')
        response = self.client.post(reverse('collection-delete', kwargs={'pk': self.collection.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Collection.objects.filter(pk=self.collection.pk).exists())












