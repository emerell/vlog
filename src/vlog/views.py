from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.utils.translation import gettext as _
from core.views import BaseView
from vlog.models import Category, Article, Tag


class IndexView(BaseView):
    template_name = 'vlog/index.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'categories': Category.get_all()[:3],
            'articles': Article.get_all()[:10],
            'tags': Tag.get_all()[:10]
        })
        return self.render_to_response(context)


class CategoriesView(BaseView):
    template_name = 'vlog/categories.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Blog')}
        ]

        context.update({
            'categories': Category.get_all(),
            'crumbs': crumbs
        })

        return self.render_to_response(context)


class CategoryView(BaseView):
    template_name = 'vlog/category.tpl'

    def get(self, request, slug, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Blog')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')}
        ]

        category = get_object_or_404(Category, slug=slug)

        article_list = Article.get_from_category(category)
        paginator = Paginator(article_list, 2)  # Show 2 articles per page

        page = request.GET.get('page')
        articles = paginator.get_page(page)

        context.update({
            'category': category,
            'top_articles': Article.get_from_category(category)[:2],
            'articles': articles,
            'crumbs': crumbs
        })

        return self.render_to_response(context)


class ArticlesView(BaseView):
    template_name = 'vlog/articles.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Blog')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')}
        ]

        context.update({
            'articles': Article.get_all(),
            'crumbs': crumbs
        })

        return self.render_to_response(context)


class ArticleView(BaseView):
    template_name = 'vlog/article.tpl'

    def get(self, request, article_slug, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        article = get_object_or_404(Article, slug=article_slug)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Blog')},
            {'url': reverse('vlog:categories'), 'title': _('Categories')},
            {'url': reverse('vlog:articles'), 'title': _('Articles')}
        ]

        context.update({
            'article': article,
            'crumbs': crumbs

        })

        return self.render_to_response(context)


class TagsView(BaseView):
    template_name = 'vlog/tags.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Blog')},
        ]
        context.update({
            'tags': Tag.get_all(),
            'articles': Article.get_all()[:3],
            'crumbs': crumbs
        })

        return self.render_to_response(context)


class TagView(BaseView):
    template_name = 'vlog/tag.tpl'

    def get(self, request, slug, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        crumbs = [
            {'url': reverse('vlog:index'), 'title': _('Blog')},
            {'url': reverse('vlog:tags'), 'title': _('Tags')}
        ]

        tag = get_object_or_404(Tag, slug=slug)

        context.update({
            'tag': tag,
            'crumbs': crumbs
        })

        return self.render_to_response(context)