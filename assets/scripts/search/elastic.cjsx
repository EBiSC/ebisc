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

    buildAgg = (facet) ->
        terms:
            field: facet.name
            order: _term: 'asc'
            size: 1000

    if not Config.facets.length
        return {}

    else
        facets:
            global: {}
            aggs: _.object([facet.name, buildAgg(facet)] for facet in Config.facets)

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
                  "Control",
                  "Foo"
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
          "terms": {
            "field": "celllinecelltype",
            "order": {
              "_term": "asc"
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
