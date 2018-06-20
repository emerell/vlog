from django.urls import path, re_path

from vlog import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r"^categories/(?P<slug>[\w-]+[']*)/$", views.CategoryView.as_view(), name='category'),
    re_path(r"^categories/(?P<category_slug>[\w-]+[']*)/articles/(?P<article_slug>[\w-]+[']*)/$",
            views.ArticleView.as_view(), name='article'),
    re_path(r'^categories/$', views.CategoriesView.as_view(), name='categories'),
    re_path(r'^articles/$', views.ArticlesView.as_view(), name='articles'),
    re_path(r"^tags/(?P<slug>[\w-]+[']*)/$", views.TagView.as_view(), name='tag'),
    re_path(r'^tags/$', views.TagsView.as_view(), name='tags'),
]