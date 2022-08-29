from rest_framework import serializers
from OrgLink.models import OrgLink

class OrgLinkSeializer(serializers.ModelSerializer):
    class Meta:
        model = OrgLink
        field = [
            'id',
            'title',
            'description',
            'url',
            'slug',            
        ]
        depth = 3
        fields = '__all__'