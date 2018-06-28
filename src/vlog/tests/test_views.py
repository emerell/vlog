from django.test import TestCase
from django.test import Client
import datetime
from vlog import views
from vlog.models import Article, Category, Comment, Tag
from django.urls import reverse


class VlogViewsTestCase(TestCase):

    def test_details(self):
        # c = Client()
        response = self.client.post('/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        client = Client()
        response = client.get(reverse('vlog:index'))
        self.assertEquals(response.status_code, 200)