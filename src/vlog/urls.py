from django.urls import path, re_path

from vlog import views

urlpatterns = [
    re_path('^$', views.IndexView.as_view(), name='index'),
    re_path(r'^categories/(?P<slug>[\w-]+)/$', views.CategoryView.as_view(), name='category'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    re_path(r'^tags/(?P<slug>[\w-]+)/$', views.TagView.as_view(), name='tags'),
    path('tags/', views.TagsView.as_view(), name='tags'),
]
