from rest_framework import serializers

from .models import Product, ProductVariant, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data('id', instance.id)
        instance.name = validated_data('name', instance.name)
        instance.image = validated_data('image', instance.image)
        instance.save()
        return instance


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'size', 'color', 'color_code']

    def create(self, validated_data):
        variant = ProductVariant.objects.create(
            id=validated_data.id,
            name=validated_data.name,
            size=validated_data.size,
            color=validated_data.color,
            color_code=validated_data.color_code
        )
        return variant

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.color = validated_data.get('color', instance.color)
        instance.color_code = validated_data.get('color_code', instance.color_code)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    variant = ProductVariantSerializer(many=True)
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'image', 'gender', 'variant', 'category']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('nam`eqqe', instance.name)
        instance.sku = validated_data.get('sku', instance.sku)
        instance.image = validated_data.get('image', instance.image)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
