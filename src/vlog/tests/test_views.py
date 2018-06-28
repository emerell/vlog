from django.test import TestCase, override_settings
from django.test import Client
import datetime
from vlog import views
from vlog.models import Article, Category, Comment, Tag
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class VlogViewsTestCase(TestCase):
    fixtures = ['vlog_views_testdata.json']

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            password='qwerty123'
        )

    def test_view_url_by_name(self):

        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)
        response = self.client.get(reverse('vlog:index'))
        self.assertEquals(response.status_code, 200)

        # import ipdb
        # ipdb.set_trace()

        self.assertTrue('categories' in response.context)