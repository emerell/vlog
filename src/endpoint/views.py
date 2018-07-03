from vlog.models import Category, Article, Tag
from endpoint.serializers import CategorySerializer, ArticleSerializer, TagSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class CategoryDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, slug):
#         try:
#             return Category.objects.get(slug=slug)
#         except Category.DoesNotExist:
#             raise Http404
#
#     def get(self, request, slug, format=None):
#         snippet = self.get_object(slug)
#         serializer = CategorySerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, slug, format=None):
#         snippet = self.get_object(slug)
#         serializer = CategorySerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, slug, format=None):
#         snippet = self.get_object(slug)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


