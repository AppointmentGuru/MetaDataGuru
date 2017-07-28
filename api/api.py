from rest_framework import routers, serializers, viewsets, filters
from .models import LineItem
from .filters import ObjectOverlapFilterBackend, IsOwnerFilterBackend

class LineItemSerializer(serializers.ModelSerializer):
    '''
    {"object_ids": [], "fields": ["name", "description", "price"], "values": [["foo", "bar", "1000"], ["baz", "bus", "3000"]], "owners": [1]}
    '''
    class Meta:
        model = LineItem
        fields = '__all__'

class LineItemViewSet(viewsets.ModelViewSet):
    queryset = LineItem.objects.all()
    serializer_class = LineItemSerializer

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        IsOwnerFilterBackend,
        ObjectOverlapFilterBackend)

    # search_fields = ('name', 'description')
    # ordering_fields = ('name',)
    ordering = ('-id',)


router = routers.DefaultRouter()
router.register(r'lineitems', LineItemViewSet)

