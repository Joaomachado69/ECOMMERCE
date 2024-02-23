from elasticsearch import Elasticsearch
from django.conf import settings

es = Elasticsearch([{'host': settings.ELASTICSEARCH_HOST, 'port': settings.ELASTICSEARCH_PORT}])

def search_products(query):
    search_body = {
        'query': {
            'multi_match': {
                'query': query,
                'fields': ['name', 'description']  
            }
        }
    }
    response = es.search(index='products', body=search_body)
    return [hit['_source'] for hit in response['hits']['hits']]
