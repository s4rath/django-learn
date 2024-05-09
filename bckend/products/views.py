from rest_framework import generics, permissions, mixins
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
# from bckend.api.permissions import IsStaffEditorPermissions
from api.mixins import StaffEditorPermissionMixin


class ProductDetailAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

class ProductUpdateAPIView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]


    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title


class ProductDestroyAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]


    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)

class ProductTitleSearchAPIView(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductListCreateAPIView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermissions]

    def perform_create(self, serializer):

        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self,request,*args,**kwargs):  #HTTP -> get
        print(args,kwargs)
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(self,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):

        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view"
        serializer.save(content=content)











# @api_view(['GET','POST'])
# def product_alt_view(request,pk=None,*args,**kwargs):
#     method= request.method
#
#     if method=="GET":
#         if pk is not None:
#
#             obj=get_object_or_404(Product,pk=pk)
#             data=ProductSerializer(obj,many=False).data
#             return Response(data)
#
#         qs= Product.objects.all()
#         data=ProductSerializer(qs,many=True,).data
#         return Response(data)
#
#     if method=="POST":
#         data = request.data
#
#         serializer = ProductSerializer(data=data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)