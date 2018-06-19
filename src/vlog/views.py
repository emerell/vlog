from django.shortcuts import get_object_or_404
from django.http import Http404
from vlog.models import Category, Article, Tag
from django.db.models import Count
from core.views import BaseView


class IndexView(BaseView):
    template_name = 'vlog/index.tpl'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        top_categories = Category.objects.annotate(articles_count=Count('articles')).order_by('-articles_count')[:3]
        top_articles = Article.objects.annotate(comments_count=Count('comments')).order_by('-comments_count')[:10]
        top_tags = Tag.objects.annotate(articles_count=Count('articles')).order_by('-articles_count')[:10]

        context.update({'categories': top_categories,
                        'articles': top_articles,
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

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(slug='slug')
        articles = Article.objects.filter(category_id=category.id).annotate(comments_count=Count('comments'))\
                .order_by('-comments_count')[:2]

        context.update({
            'category': category,
            'articles': articles,
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

        article = Article.objects.get(id=kwargs.get('article_id'))

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

        # tag = Tag.objects.get(id=kwargs.get('tag_id'))
        # articles = Article.objects.filter(tag_id=tag.id).annotate(comments_count=Count('comments'))\
        #     .order_by('-comments_count')

        try:
            tag = Tag.objects.get(id=kwargs.get('slug'))
        except Tag.DoesNotExist:
            raise Http404("No Tag matches the given query.")
        articles = Article.objects.annotate(comments_count=Count('comments')).order_by('-comments_count')[:3]
        context.update({
            'tag': tag,
            'articles': articles,
        })

        return self.render_to_response(context)


