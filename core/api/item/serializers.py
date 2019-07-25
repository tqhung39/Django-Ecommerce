from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from core.models import Item


class ItemListSerializer(ModelSerializer):
    user = SerializerMethodField()
    url = HyperlinkedIdentityField(
        view_name='core-api-item:detail',
        lookup_field='slug'
    )
    delete_url = HyperlinkedIdentityField(
        view_name='core-api-item:delete',
        lookup_field='slug'
    )

    class Meta:
        model = Item
        fields = '__all__'

    def get_user(self, obj):
        return str(obj.user.username)


class ItemDetailSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Item
        fields = '__all__'

    def get_user(self, obj):
        return str(obj.user.username)


class ItemCreateUpdateSerializer(ModelSerializer):
    item_url = HyperlinkedIdentityField(
        view_name='core-api-item:detail',
        lookup_field='slug'
    )

    class Meta:
        model = Item
        fields = '__all__'
