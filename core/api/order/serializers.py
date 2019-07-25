from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from core.models import Order, OrderItem, Item, Coupon
from core.api.orderitem.serializers import OrderItemListSerializer
from core.api.coupon.serializers import CouponListSerializer


class OrderListSerializer(ModelSerializer):
    user = SerializerMethodField()
    shipping_address = SerializerMethodField()
    url = HyperlinkedIdentityField(
        view_name='core-api-order:detail',
        lookup_field='shipping_address'
    )

    class Meta:
        model = Order
        fields = '__all__'

    def get_user(self, obj):
        return str(obj.user.username)

    def get_shipping_address(self, obj):
        return str(obj.shipping_address.street_address)


class OrderDetailSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
