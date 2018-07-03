from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from vlog.models import Category, Article, Tag
from .serializers import CategorySerializer, ArticleSerializer, TagSerializer
from django.utils import timezone
from django.contrib.auth import get_user_model


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_category(id, title, slug, image, author_id):
        Category.objects.create(
            id=id, title=title, slug=slug, created=timezone.now(),
            updated=timezone.now(), image=image, author_id=author_id)

    @staticmethod
    def create_article(id, title, slug, author_id, category_id, description="", content=""):
        Article.objects.create(
            id=id, title=title, slug=slug, created=timezone.now(), content=content,
            updated=timezone.now(), description=description, author_id=author_id, category_id=category_id)

    @staticmethod
    def create_tag(id, title, slug):
        Tag.objects.create(
            id=id, title=title, slug=slug, created=timezone.now(), updated=timezone.now())

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            password='qwerty123'
        )
        # add test data
        self.create_category(1, "food", "food", None,  self.user.pk)
        self.create_category(2, "sport", "sport", None,  self.user.pk)
        self.create_article(1, "About food", "about-food", self.user.pk, 1)
        self.create_article(2, "About sport", "about-sport", self.user.pk, 2)
        self.create_tag(2, "tag", "tag")


class CategoriesTest(BaseViewTest):

    def test_get_all_categories(self):
        """
        This test ensures that all categories added in the setUp method
        exist when we make a GET request to the endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("endpoint:categories", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Category.objects.all()
        serialized = CategorySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_category(self):
    #     # hit the API endpoint
    #     response = self.client.get(
    #         reverse("endpoint:category", kwargs={"slug": "sport", "version": "v1"})
    #     )
    #     # fetch the data from db
    #     expected = Category.objects.get(slug="sport")
    #
    #     serialized = CategorySerializer(expected, many=True)
    #     self.assertEqual(response.data, serialized.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class ArticlesTest(BaseViewTest):

    def test_get_all_articles(self):
        response = self.client.get(
            reverse("endpoint:articles", kwargs={"version": "v1"})
        )
        expected = Article.objects.all()
        serialized = ArticleSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TagsTest(BaseViewTest):

    def test_get_all_articles(self):
        response = self.client.get(
            reverse("endpoint:tags", kwargs={"version": "v1"})
        )
        expected = Tag.objects.all()
        serialized = TagSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)