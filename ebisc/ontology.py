import os
import urllib
import requests


def memoize(f):

    class memodict(dict):
        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret

    return memodict(f)


BASE_URL = 'http://www.ebi.ac.uk/ols/beta/api/ontologies/efo/'
HEADERS = {'Accept': 'application/json'}


def encode_purl(purl):
    return urllib.quote(urllib.quote(purl, safe=''), safe='')


@memoize
def term_of_purl(purl):
    return requests.get(os.path.join(BASE_URL, 'terms', encode_purl(purl)), HEADERS).json()


def label_of_purl(purl):
    return term_of_purl(purl).get('label', None)


@memoize
def ancestor_terms_of_purl(purl):
    return requests.get(os.path.join(BASE_URL, 'terms', encode_purl(purl), 'ancestors'), HEADERS).json()['_embedded']['terms']


def ancestor_labels_of_purl(purl):
    return [term['label'] for term in ancestor_terms_of_purl(purl)]


'''

Term http://purl.obolibrary.org/obo/CL_0002551

{
  "obo_id": "CL:0002551",
  "description": [
    "fibroblast that is part of dermis"
  ],
  "ontology_prefix": "EFO",
  "is_obsolete": false,
  "has_children": false,
  "ontology_iri": "http://www.ebi.ac.uk/efo",
  "label": "fibroblast of dermis",
  "is_root": false,
  "iri": "http://purl.obolibrary.org/obo/CL_0002551",
  "synonyms": [
    "dermal fibroblast"
  ],
  "_links": {
    "part_of": {
      "href": "http://www.ebi.ac.uk/ols/beta/api/ontologies/efo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0002551/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000050"
    },
    "ancestors": {
      "href": "http://www.ebi.ac.uk/ols/beta/api/ontologies/efo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0002551/ancestors"
    },
    "graph": {
      "href": "http://www.ebi.ac.uk/ols/beta/api/ontologies/efo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0002551/graph"
    },
    "self": {
      "href": "http://www.ebi.ac.uk/ols/beta/api/ontologies/efo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0002551"
    },
    "jstree": {
      "href": "http://www.ebi.ac.uk/ols/beta/api/ontologies/efo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0002551/jstree"
    },
    "parents": {
      "href": "http://www.ebi.ac.uk/ols/beta/api/ontologies/efo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0002551/parents"
    }
  },
  "is_defining_ontology": false,
  "annotation": {
    "definition_editor": [
      "Sirarat Sarntivijai"
    ],
    "has_obo_namespace": [
      "cell"
    ],
    "created_by": [
      "tmeehan"
    ],
    "creation_date": [
      "2011-02-28T05:05:33Z"
    ]
  },
  "ontology_name": "efo",
  "short_form": "CL_0002551"
}

'''
