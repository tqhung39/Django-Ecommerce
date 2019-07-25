from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from core.models import OrderItem


class OrderItemListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='core-api-orderitem:detail',
        lookup_field='user'
    )

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemDetailSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
