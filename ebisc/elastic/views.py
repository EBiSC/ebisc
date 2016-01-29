import json
from functools import partial
from elasticsearch import Elasticsearch, ElasticsearchException

from django.http import Http404, JsonResponse, HttpResponseNotAllowed
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

es = Elasticsearch(settings.ELASTIC_HOSTS)


ENDPOINTS = {
    'ebisc/cellline/_search': {
        'methods': ['POST'],
        'action': partial(es.search, index='ebisc', doc_type='cellline')
    }
}


@csrf_exempt
def endpoint(request, path):

    if path not in ENDPOINTS:
        raise Http404

    endpoint = ENDPOINTS[path]

    if endpoint.get('methods', None) and request.method not in endpoint.get('methods', []):
        return HttpResponseNotAllowed(endpoint.get('methods'))

    try:
        res = endpoint['action'](body=json.loads(request.body))
    except ElasticsearchException, e:
        return JsonResponse(e.info, status=e.status_code)
    except Exception:
        return JsonResponse({}, status=500)

    return JsonResponse(res)
