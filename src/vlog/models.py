from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from django.db.models import Count
from ckeditor.fields import RichTextField
from core.models import BaseModel


class Publication(BaseModel):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Title')
    )

    slug = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        verbose_name=_('Slug')
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Category(Publication):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='categories',
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        null=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )

    @classmethod
    def get_all(cls):
        return cls.objects.annotate(articles_count=Count('articles')).order_by('-articles_count')

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Article(Publication):
    description = models.CharField(
        max_length=200,
        verbose_name=_('Description')
    )

    content = RichTextField()

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='articles',
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        null=True
    )

    category = models.ForeignKey(
        to='Category',
        related_name='articles',
        verbose_name=_('Category'),
        on_delete=models.SET_NULL,
        null=True
    )

    @classmethod
    def get_all(cls):
        return cls.objects.annotate(comments_count=Count('comments')).order_by('-comments_count')

    @classmethod
    def get_from_category(cls, category):
        return cls.objects.filter(category_id=category.id).annotate(
            comments_count=Count('comments')).order_by('-comments_count')

    class Meta:
        db_table = 'article'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')


class Tag(Publication):
    articles = models.ManyToManyField(
        to='Article',
        related_name='tags',
        verbose_name=_('Articles')
    )

    @classmethod
    def get_all(cls):
        return cls.objects.annotate(articles_count=Count('articles')).order_by('-articles_count')

    class Meta:
        db_table = 'tag'
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Comment(BaseModel):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='comments',
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        null=True
    )

    article = models.ForeignKey(
        to='Article',
        related_name='comments',
        verbose_name=_('Article'),
        on_delete=models.SET_NULL,
        null=True
    )

    text = models.TextField(
        verbose_name=_('Text')
    )

    def __str__(self):
        return f'{self.author.username} [{self.article.title}]'

    class Meta:
        db_table = 'comment'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
