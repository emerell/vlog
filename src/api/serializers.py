from rest_framework import serializers
from vlog.models import Category, Article, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'title', 'slug', 'created', 'updated', 'image', 'author_id'
                  )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id', 'title', 'slug', 'description', 'content',
            'created', 'updated', 'author_id', 'category_id'
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id', 'title', 'slug', 'created', 'updated'
        )
