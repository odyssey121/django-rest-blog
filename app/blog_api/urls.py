from django.conf.urls import url
from django.urls import path, include
from .views import ArticlesGenericView, CategoryGenericView, ArticleGenericView, TagGenericView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticlesGenericView, basename='articles')
router.register('categories', CategoryGenericView, basename='categories')
router.register('tags', TagGenericView, basename='tags')

urlpatterns = [
    path('article/<int:id>/', ArticleGenericView.as_view()),
    url('', include(router.urls)),
]
