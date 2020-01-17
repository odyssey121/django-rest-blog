from rest_framework.relations import PrimaryKeyRelatedField

from .models import Article, Category
from rest_framework import serializers


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

    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'author', 'categories', )
        read_only_fields = ('id', 'author')
