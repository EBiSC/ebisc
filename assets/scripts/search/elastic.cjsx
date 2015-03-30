XRegExp = require('xregexp').XRegExp

State = require './state'
Config = require './config'

elastic = window.elasticsearch.Client
    hosts: 'localhost:9200'

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
  "query": {
    "filtered": {
      "query": {
        "bool": {
          "must": [
            {
              "multi_match": {
                "query": "control",
                "type": "phrase_prefix",
                "fields": [
                  "biosamplesid",
                  "celllinename",
                  "celllinecelltype.analyzed",
                  "celllineprimarydisease.analyzed"
                ]
              }
            },
            {
              "multi_match": {
                "query": "derma",
                "type": "phrase_prefix",
                "fields": [
                  "biosamplesid",
                  "celllinename",
                  "celllinecelltype.analyzed",
                  "celllineprimarydisease.analyzed"
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
                  "Control"
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
        "celllinetypes": {
          "filter": {
            "bool": {
              "must": [
                {
                  "terms": {
                    "celllineprimarydisease": [
                      "Control"
                    ]
                  }
                }
              ]
            }
          },
          "aggs": {
            "facet": {
              "terms": {
                "field": "celllinecelltype",
                "size": 100,
                "order": {
                  "_term": "asc"
                }
              }
            }
          }
        },
        "diseases": {
          "terms": {
            "field": "celllineprimarydisease",
            "order": {
              "_term": "asc"
            }
          }
        }
      }
    }
  }
}

'''
# -----------------------------------------------------------------------------
