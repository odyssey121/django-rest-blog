from rest_framework.relations import PrimaryKeyRelatedField

from .models import Article, Category, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # queryset = Category.objects.all()

    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     super(ArticleSerializer, self).__init__(*args, **kwargs)
    #     if 'request' in self.context and self.context['view'].request.method == 'GET':
    #         self.fields['categories'] = 'fsdfsd'

    author = serializers.StringRelatedField()
    categories = serializers.SlugRelatedField(
        many=True, slug_field='name', read_only=False, queryset=Category.objects.all()
    )
    tags = serializers.SlugRelatedField(
        many=True, slug_field='name', read_only=False, queryset=Tag.objects.all()
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'author', 'categories', 'tags')
        read_only_fields = ('id', 'author')
