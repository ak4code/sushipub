from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    link = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Category
        fields = '__all__'
