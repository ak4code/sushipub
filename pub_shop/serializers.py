from rest_framework import serializers

from .models import Category, Product, Ingredient


class CategorySerializer(serializers.ModelSerializer):
    link = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    link = serializers.CharField(source='get_absolute_url', read_only=True)
    ingredient_list = IngredientSerializer(source='ingredients', many=True, read_only=True)
    category_info = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
