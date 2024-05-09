from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    # edit_url=serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field='pk')
    title= serializers.CharField(validators=[validators.validate_title_no_hello,
                                             validators.unique_product_title])
    # name=serializers.CharField(source="title",read_only=True)
    class Meta:
        model = Product
        fields =[
            'url',
            # 'edit_url',
            'pk',
            'title',
            # 'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def validate_title(self,value):
        request = self.context.get('request')
        user = request.user
        qs= Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value

    # def get_edit_url(self,obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # def get_url(self,obj):
    #     # return f"/api/products/{obj.pk}/"
    #     request=self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-detail", kwargs={"pk":obj.pk},request=request)

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None


