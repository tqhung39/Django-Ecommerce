from rest_framework.serializers import ModelSerializer
from core.models import Item


class ItemListSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemDetailSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
