import json
from students.models import Students

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import *
from .elastic import *


class PublisherDocumentSerializer(DocumentSerializer):
    """Serializer for Publisher document."""
    #location = serializers.SerializerMethodField()

    class Meta(object):
        """Meta options."""
        model = Students
        document = PublisherDocument
        fields = (
            'registration_number',
            'first_name',
            'last_name',
            'gender',
            'date_of_admission',
            'created_at'
            
        )
        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}