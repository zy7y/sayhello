#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
"""
@Project: say
@File  :serializers.py
@Author:zy7y
@Date  :2021/6/2 14:28
@Desc  : 序列化文件
"""
from django.contrib.auth.models import User, Group

from .models import Text
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'  # 3.3 之后被弃用 需要显式定义

