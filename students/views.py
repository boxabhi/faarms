

from django.shortcuts import render, resolve_url
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)
from .serializers import PublisherDocumentSerializer
from .models import Students


from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .elastic import PublisherDocument
from faker import Faker
fake = Faker()
from datetime import date, datetime
import random
from django.http import JsonResponse
import random
import time

def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)


from .documents import CarDocument

def generate_fake(request):
    students = PublisherDocument.search()
    
    if request.GET.get('sort'):
        students = students.sort("id" )
        
    
    if request.GET.get('registration_number'):
        students = students.filter("match" ,  registration_number= request.GET.get('registration_number'))
        
    
    if request.GET.get('first_name'):
        students = students.filter("wildcard" ,  first_name= request.GET.get('first_name'))
    
    if request.GET.get('date_of_admission'):
        students = students.filter("range" ,  date_of_admission= {'lte': datetime.now()})
        
        
    
    response = students.execute()
    payload = []
    print(response)
    for hit in response:
        payload.append({
            'first_name' : hit.first_name,
            'last_name' : hit.last_name,
            "registration_number" :hit.registration_number
            
        })
        print(hit.first_name)
        

    
 
    # for i in range(100):
    #     Students.objects.create(
    #         first_name = fake.name(),
    #         last_name = fake.name(),
    #         gender = fake.name(),
    #         date_of_admission = random_date("2010-1-1", "2021-1-2", random.random())
    #     )
    
    return JsonResponse({'status' : 200 , 'len' : len(response) , 'payload' : payload})
        


class PublisherDocumentView(DocumentViewSet):
    document = PublisherDocument
    serializer_class = PublisherDocumentSerializer
    lookup_field = 'first_name'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,

        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
   
    search_fields = (
        'registration_number',
        'first_name',
        'last_name',
        'gender',
        'date_of_admission',
    )
    multi_match_search_fields = (
       'registration_number',
        'first_name',
        'last_name',
        'gender',
        'date_of_admission',
    )
    filter_fields = {
        'id': None,
        'registration_number' : 'registration_number',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'gender': 'gender',
    }
    ordering_fields = {
        'id': None,
        'date_of_admission' : None ,
        'created_at' : None,
    }
    ordering = ( 'date_of_admission'  ,)
    
    

def index(request):
    return render(request, 'index.html')