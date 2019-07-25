from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from core.models import Coupon


class CouponListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='core-api-coupon:detail',
        lookup_field='code'
    )

    class Meta:
        model = Coupon
        fields = '__all__'


class CouponDetailSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class CouponCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
