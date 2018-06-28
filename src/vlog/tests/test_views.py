from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class VlogViewsTestCase(TestCase):
    fixtures = ['vlog_views_testdata.json']

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            password='qwerty123'
        )

    def test_index_view(self):

        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)
        response = self.client.get(reverse('vlog:index'))
        self.assertEquals(response.status_code, 200)

        self.assertTrue('categories' in response.context_data)
        self.assertTrue('articles' in response.context_data)
        self.assertTrue('tags' in response.context_data)

        self.assertEqual([category.pk for category in response.context_data['categories']], [2, 3, 1])
        self.assertEqual([category.title for category in
                          response.context_data['categories']], ['Food', 'Art', 'Sport'])

    def test_categories_view(self):

        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)
        response = self.client.get(reverse('vlog:categories'))
        self.assertEquals(response.status_code, 200)

        self.assertTrue('categories' in response.context_data)
        self.assertEqual([category.title for category in
                          response.context_data['categories']], ['Food', 'Art', 'Sport'])

    def test_tags_view(self):

        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)
        response = self.client.get(reverse('vlog:tags'))
        self.assertEquals(response.status_code, 200)

        self.assertTrue('articles' in response.context_data)
        self.assertTrue('tags' in response.context_data)
        self.assertEqual([article.pk for article in
                         response.context_data['articles']], [2, 3, 1])
        self.assertEqual([tag.title for tag in
                          response.context_data['tags']], ['tag3', 'tag2', 'tag1'])

    def test_article_view(self):

        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)
        response = self.client.get(reverse('vlog:article',
                                   kwargs={'category_slug': 'sport', 'article_slug': 'about-sport'}))
        self.assertEquals(response.status_code, 200)

        self.assertTrue('article' in response.context_data)
        self.assertEqual(response.context_data['article'].title, 'About sport')

    def test_tag_view(self):

        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)
        response = self.client.get(reverse('vlog:tag',
                                           kwargs={'slug': 'tag1'}))
        self.assertEquals(response.status_code, 200)

        self.assertTrue('tag' in response.context_data)
        self.assertEqual(response.context_data['tag'].title, 'tag1')

    def test_tag_view(self):
        response = self.client.login(
            username='user',
            password='qwerty123'
        )
        self.assertTrue(response)

        response = self.client.get(reverse('vlog:category',
                                           kwargs={'slug': 'art'}))
        self.assertEquals(response.status_code, 200)

        self.assertTrue('category' in response.context_data)
        self.assertEqual(response.context_data['category'].title, 'Art')