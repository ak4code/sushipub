from pprint import pprint

from rest_framework import serializers

from .models import Category, Product, Ingredient, Destination, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    link = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'weight', 'size', 'image')


class ProductSerializer(serializers.ModelSerializer):
    link = serializers.CharField(source='get_absolute_url', read_only=True)
    ingredient_list = IngredientSerializer(source='ingredients', many=True, read_only=True)
    category_info = CategorySerializer(source='category', read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductOrderSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'image', 'price')
        read_only_fields = ('name', 'category', 'image', 'price')


class ProductPKField(serializers.RelatedField):

    def to_internal_value(self, data):
        return self.get_queryset().get(pk=data['id'])

    def to_representation(self, value):
        obj = {
            'id': value.pk,
            'name': value.name,
            'category': value.category.name,
            'image': self.context['request'].build_absolute_uri(value.image.url),
            'price': value.price
        }
        return obj


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    product = ProductPKField(queryset=Product.objects.all())
    amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, )
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items:
            OrderItem.objects.create(order=order, **item)
        return order
