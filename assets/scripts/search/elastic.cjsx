XRegExp = require('xregexp').XRegExp

State = require './state'
Config = require './config'

if window.location.hostname in ['127.0.0.1', 'localhost']
    elasticSearchHost = '127.0.0.1:9200'
else
    elasticSearchHost = window.location.hostname + '/db'

elastic = window.elasticsearch.Client
    hosts: elasticSearchHost

# -----------------------------------------------------------------------------
# Search

search = () ->

    body =
        size: 1000
        query: buildFilteredQuery()
        aggs: buildAggregations()

    # console.debug '-- QUERY BODY --'
    # console.debug JSON.stringify(body, null, '  ')

    elastic.search
        index: 'ebisc'
        type: 'cellline'
        body: body

    .then (body) ->
        State.set('celllines', body.hits.hits)
        State.set('facetTerms', body.aggregations.facets)
        State.set('isLoaded', true)

    .error (error) ->
        alert('Error loading data.')

# -----------------------------------------------------------------------------
# Filtered query

buildFilteredQuery = () ->

    filtered:
        query: buildQuery()
        filter: buildFilter()

# -----------------------------------------------------------------------------
# Query

buildQuery = () ->

    queryString = _.trim(State.select('filter', 'query').get().toLowerCase())

    if not queryString
        return match_all: {}

    else
        words = (w for w in XRegExp.split(queryString, XRegExp('[^(\\p{L}|\\d)]')) when w != '')

        buildQueryMultiMatch = (word, fields) ->
            multi_match:
                query: word
                type: 'phrase_prefix'
                fields: fields

        bool:
            must: (buildQueryMultiMatch(word, Config.query_fields) for word in words)

# -----------------------------------------------------------------------------
# Filters

buildFilter = () ->

    filters = buildFacetFilters()

    if not filters
        return {}
    else
        bool:
            must: filters

buildFacetFilters = () ->

    buildTerms = (terms) ->
        (term for term, selected of terms when selected == true)

    (terms: "#{facet.name}": buildTerms(facet.selectedTerms) for facet in State.select('filter', 'facets').get() when buildTerms(facet.selectedTerms).length)


# -----------------------------------------------------------------------------
# Aggregations

buildAggregations = () ->

    facets = State.select('filter', 'facets').get()

    if not facets.length
        return {}

    else
        buildAgg = (facet, filters) ->

            # If there are filters for other facets, use them to filter this facet (but do not use filter for this facet)
            otherFilters = (filter for filter in filters when not (facet.name of filter.terms))

            # If there is a query, use it to filter this facet
            query = buildQuery()
            if 'bool' of query
                for match in query.bool.must
                    otherFilters.push query: match

            terms =
                field: facet.name
                order: _term: 'asc'
                size: 0

            if not otherFilters.length
                terms: terms

            else
                filter:
                    bool:
                        must: otherFilters
                aggs:
                    facet:
                        terms: terms

        filters = buildFacetFilters()

        facets:
            global: {}
            aggs: _.object([facet.name, buildAgg(facet, filters)] for facet in facets)

# -----------------------------------------------------------------------------

module.exports =
    search: search

# -----------------------------------------------------------------------------
# Example query

'''

GET /ebisc/cellline/_search
{
  "size": 1000,
  "query": {
    "filtered": {
      "query": {
        "bool": {
          "must": [
            {
              "multi_match": {
                "query": "unass",
                "type": "phrase_prefix",
                "fields": [
                  "biosamplesid",
                  "celllinename",
                  "depositor.analyzed",
                  "celllinecelltype.analyzed",
                  "celllineprimarydisease.analyzed",
                  "celllinenamesynonyms"
                ]
              }
            }
          ]
        }
      },
      "filter": {
        "bool": {
          "must": [
            {
              "terms": {
                "celllineprimarydisease": [
                  "Hereditary spastic Paraplegia: SPG4"
                ]
              }
            },
            {
              "terms": {
                "depositor": [
                  "UKB"
                ]
              }
            }
          ]
        }
      }
    }
  },
  "aggs": {
    "facets": {
      "global": {},
      "aggs": {
        "celllineprimarydisease": {
          "filter": {
            "bool": {
              "must": [
                {
                  "terms": {
                    "depositor": [
                      "UKB"
                    ]
                  }
                },
                {
                  "query": {
                    "multi_match": {
                      "query": "unass",
                      "type": "phrase_prefix",
                      "fields": [
                        "biosamplesid",
                        "celllinename",
                        "depositor.analyzed",
                        "celllinecelltype.analyzed",
                        "celllineprimarydisease.analyzed",
                        "celllinenamesynonyms"
                      ]
                    }
                  }
                }
              ]
            }
          },
          "aggs": {
            "facet": {
              "terms": {
                "field": "celllineprimarydisease",
                "order": {
                  "_term": "asc"
                },
                "size": 0
              }
            }
          }
        },
        "celllinecelltype": {
          "filter": {
            "bool": {
              "must": [
                {
                  "terms": {
                    "celllineprimarydisease": [
                      "Hereditary spastic Paraplegia: SPG4"
                    ]
                  }
                },
                {
                  "terms": {
                    "depositor": [
                      "UKB"
                    ]
                  }
                },
                {
                  "query": {
                    "multi_match": {
                      "query": "unass",
                      "type": "phrase_prefix",
                      "fields": [
                        "biosamplesid",
                        "celllinename",
                        "depositor.analyzed",
                        "celllinecelltype.analyzed",
                        "celllineprimarydisease.analyzed",
                        "celllinenamesynonyms"
                      ]
                    }
                  }
                }
              ]
            }
          },
          "aggs": {
            "facet": {
              "terms": {
                "field": "celllinecelltype",
                "order": {
                  "_term": "asc"
                },
                "size": 0
              }
            }
          }
        },
        "depositor": {
          "filter": {
            "bool": {
              "must": [
                {
                  "terms": {
                    "celllineprimarydisease": [
                      "Hereditary spastic Paraplegia: SPG4"
                    ]
                  }
                },
                {
                  "query": {
                    "multi_match": {
                      "query": "unass",
                      "type": "phrase_prefix",
                      "fields": [
                        "biosamplesid",
                        "celllinename",
                        "depositor.analyzed",
                        "celllinecelltype.analyzed",
                        "celllineprimarydisease.analyzed",
                        "celllinenamesynonyms"
                      ]
                    }
                  }
                }
              ]
            }
          },
          "aggs": {
            "facet": {
              "terms": {
                "field": "depositor",
                "order": {
                  "_term": "asc"
                },
                "size": 0
              }
            }
          }
        }
      }
    }
  }
}

'''
# -----------------------------------------------------------------------------
