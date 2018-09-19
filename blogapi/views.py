from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import ArticleSerializer, UserSerializer, GroupSerializer

# Create your views here.


def index(request):
    article_list = Article.objects.all()[:1]
    print(article_list)
    return HttpResponse(article_list)


class ArticleViewSet(viewsets.ModelViewSet):
    '''
    获取文章信息的api
    '''
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users tobe viewed or edited.
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
