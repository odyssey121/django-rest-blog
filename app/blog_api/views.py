from rest_framework import filters
from rest_framework import generics, status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters
from .permissions import IsAuthorOfPost
from rest_framework import permissions


# Create your views here.

class CategoryGenericView(viewsets.GenericViewSet, mixins.ListModelMixin, ):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    auth_methods = ('create', 'put', 'delete',)

    def get_permissions(self):
        if self.action in self.auth_methods:
            permission_classes = [IsAdminUser, ]
            return [permission() for permission in permission_classes]
        return list()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticlesGenericView(viewsets.GenericViewSet, mixins.ListModelMixin,
                          mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = (TokenAuthentication,)
    # filter_backends = [filters.SearchFilter]
    auth_methods = ('create', 'put', 'delete',)
    search_fields = ['author']

    def get_permissions(self):
        if self.action in self.auth_methods:
            permission_classes = [IsAuthenticated, ]
            return [permission() for permission in permission_classes]
        return list()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            author = self.request.user
        except Exception as error:
            print(error)
            content = {'error': 'author not found or user is not autheticated'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        serializer.save(author=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleGenericView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                         mixins.ListModelMixin, mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    lookup_field = 'id'
    queryset = Article.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            permission_classes = [IsAuthorOfPost]
            return [permission() for permission in permission_classes]
        return [IsAuthenticated()]

    def get(self, request, id=None, *args, **kwargs):
        if id is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
