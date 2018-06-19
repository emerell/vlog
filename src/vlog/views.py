from django.shortcuts import get_object_or_404
from django.http import Http404
from vlog.models import Category, Article, Tag
from django.db.models import Count
from core.views import BaseView
from django.urls import reverse
from django.utils.translation import gettext as _


class IndexView(BaseView):
    template_name = 'vlog/index.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        top_categories = Category.objects.annotate(articles_count=Count('articles')).order_by('-articles_count')[:3]
        top_tags = Tag.objects.annotate(articles_count=Count('articles')).order_by('-articles_count')[:10]

        context.update({
            'categories': top_categories,
            'articles': Article.get_top(),
            'tags': top_tags
        })
        return self.render_to_response(context)


class CategoriesView(BaseView):
    template_name = 'vlog/categories.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.annotate(articles_count=Count('articles')).order_by('-articles_count')

        context.update({
            'categories': categories
        })

        return self.render_to_response(context)


class CategoryView(BaseView):
    template_name = 'vlog/category.tpl'

    def get(self, request, slug, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Home')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')}
        ]

        category = get_object_or_404(Category, slug=slug)

        articles = Article.objects.filter(
            category_id=category.id
        ).annotate(
            comments_count=Count('comments')
        ).order_by('-comments_count')[:2]

        context.update({
            'category': category,
            'articles': articles,
            'crumbs': crumbs
        })

        return self.render_to_response(context)


class ArticlesView(BaseView):
    template_name = 'vlog/articles.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        articles = Article.objects.annotate(comments_count=Count('comments')).order_by('-comments_count')

        context.update({
            'articles': articles
        })

        return self.render_to_response(context)


class ArticleView(BaseView):
    template_name = 'vlog/article.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(slug=kwargs.get('article_slug'))

        context.update({
            'article': article
        })

        return self.render_to_response(context)


class TagsView(BaseView):
    template_name = 'vlog/tags.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tags = Tag.objects.annotate(articles_count=Count('articles')).order_by('-articles_count')
        top_articles = Article.objects.annotate(comments_count=Count('comments')).order_by('-comments_count')[:3]

        context.update({
            'tags': tags,
            'articles': top_articles
        })

        return self.render_to_response(context)

# list of articles with category (order by comments quantity)


class TagView(BaseView):
    template_name = 'vlog/tag.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = Tag.objects.get(slug=kwargs.get('slug'))

        context.update({
            'tag': tag
        })

        return self.render_to_response(context)


