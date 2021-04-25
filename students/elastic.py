
from django_elasticsearch_dsl import (
    Document ,
    fields,
    Index,
)
from .models import Students
PUBLISHER_INDEX = Index('students')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


@PUBLISHER_INDEX.doc_type
class PublisherDocument(Document):
    
    id = fields.IntegerField(attr='id')
    fielddata=True
    registration_number = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    first_name = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    last_name = fields.TextField(
        fields={
            'raw': fields.TextField(
                analyzer='keyword'
            )
        }
    )
    gender = fields.TextField(
        fields={
            'raw': fields.TextField(
                analyzer='keyword'
            )
        }
    )
    
    date_of_admission = fields.DateField()
    created_at = fields.DateField()
    
   
   

    class Django(object):
        model = Students