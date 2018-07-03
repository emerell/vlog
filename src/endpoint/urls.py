from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from endpoint import views

urlpatterns = [
    re_path(r'^categories/$', views.CategoryList.as_view(), name='categories'),
    # re_path(r"^categories/(?P<slug>[\w-]+[']*)/$", views.CategoryDetail.as_view(), name='category'),
    re_path(r'^articles/$', views.ArticleList.as_view(), name='articles'),
    re_path(r'^tags/$', views.TagList.as_view(), name='tags'),
]

urlpatterns = format_suffix_patterns(urlpatterns)