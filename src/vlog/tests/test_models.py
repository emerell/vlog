from django.contrib.auth import get_user_model
from django.test import TestCase
from vlog.models import Article, Category, Comment, Tag


class BaseTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user', password='qwerty123'
        )

        Category.objects.create(
            id="1",
            title="tests",
            slug="tests",
            author=self.user
        )

        Article.objects.create(
            id="7",
            title="Tests in Django",
            slug="tests-in-django",
            description="Run it",
            content="This is very important test!",
            author=self.user,
            category_id = "1"
        )

        Comment.objects.create(
            id="1",
            author=self.user,
            text="some very important text",
            article_id="7"
        )

        Tag.objects.create(
            id="1",
            title="#test",
            slug="test",
        )


class ArticleModelTest(BaseTest):
    def test_article_title(self):
        art = Article.objects.get(title="Tests in Django")
        self.assertEqual(art.description, "Run it")

        art2 = Article.objects.get(id=7)
        self.assertEqual(art2.title, "Tests in Django")

    def test_article_description(self):
        art = Article.objects.get(title="Tests in Django")
        self.assertEqual(art.description, "Run it")

    def test_article_content(self):
        art = Article.objects.get(title="Tests in Django")
        self.assertEqual(art.content, "This is very important test!")

    def test_article_user(self):
        art2 = Article.objects.get(id=7)
        self.assertEqual(art2.author, self.user)

    def test_article_slug(self):
        art2 = Article.objects.get(id=7)
        self.assertEqual(art2.slug, 'tests-in-django')

    def test_str(self):
        art = Article.objects.get(title="Tests in Django")
        self.assertEqual(str(art), "Tests in Django")


class CategoryModelTest(BaseTest):
    def test_category_title(self):
        cat = Category.objects.get(id=1)
        self.assertEqual(cat.title, "tests")

    def test_article_user(self):
        cat = Category.objects.get(id=1)
        self.assertEqual(cat.author, self.user)

    def test_article_slug(self):
        cat = Category.objects.get(id=1)
        self.assertEqual(cat.slug, 'tests')


class CommentModelTest(BaseTest):
    def test_comment_user(self):
        comm = Comment.objects.get(id=1)
        self.assertEqual(comm.author, self.user)

    def test_comment_text(self):
        comm = Comment.objects.get(id=1)
        self.assertEqual(comm.text, 'some very important text')

    def test_str(self):
        comm = Comment.objects.get(id=1)
        self.assertEqual(str(comm), "user [Tests in Django]")


class CommentModelTest(BaseTest):
    def test_comment_user(self):
        comm = Comment.objects.get(id=1)
        self.assertEqual(comm.author, self.user)

    def test_comment_text(self):
        comm = Comment.objects.get(id=1)
        self.assertEqual(comm.text, 'some very important text')

    def test_str(self):
        comm = Comment.objects.get(id=1)
        self.assertEqual(str(comm), "user [Tests in Django]")


class TagModelTest(BaseTest):
    def test_tag_title(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(tag.title, "#test")

    def test_tag_slug(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(tag.slug, 'test')
