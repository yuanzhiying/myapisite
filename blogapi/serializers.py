#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'yuanzhiying'


from django.contrib.auth.models import User, Group
from .models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'info', 'author', 'articledate')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
