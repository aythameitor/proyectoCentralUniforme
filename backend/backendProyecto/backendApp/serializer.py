from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Category, MenuElements

class MenuElementSerializer(ModelSerializer):
    fileLink = serializers.FileField(max_length=None, use_url=True)

    class Meta :
        model = MenuElements
        fields = '__all__'

class CategorySerializer(ModelSerializer):

    class Meta :
        model = Category
        fields = '__all__'

