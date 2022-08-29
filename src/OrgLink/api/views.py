from statistics import quantiles
from rest_framework.viewsets import ModelViewSet
from OrgLink.api.serialiszer import OrgLinkSeializer
from OrgLink.models import OrgLink

class OrgLinkViewSet(ModelViewSet):
    queryset = OrgLink.objects.all()
    serializer_class = OrgLinkSeializer
    # serializer = OrgLinkSeializer(queryset, many=True)