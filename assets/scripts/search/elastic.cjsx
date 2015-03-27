_ = window._
Elasticsearch = window.elasticsearch

XRegExp = require('xregexp').XRegExp

State = require './state'
Config = require './config'

elastic = Elasticsearch.Client
    hosts: 'localhost:9200'

'''
Example query:

GET ebisc/cellline/_search
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
                  "Control", "Foo"
                ]
              }
            }
          ]
        }
      }
    }
  }
}
'''


buildFacetFilters = () ->

    buildTerms = (items) ->
        (item.name for item in items when item.checked)

    (terms: "#{facet.name}": buildTerms(facet.items) for facet in State.select('filter', 'facets').get() when buildTerms(facet.items).length)


buildFilter = () ->

    filters = buildFacetFilters()

    if not filters
        return {}
    else
        bool:
            must: filters


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


buildFilteredQuery = () ->

    filtered:
        query: buildQuery()
        filter: buildFilter()


search = () ->

    query = buildFilteredQuery()

    # console.debug '-- QUERY BODY --'
    # console.debug JSON.stringify(query, null, ' ')

    elastic.search
        index: 'ebisc'
        type: 'cellline'
        body:
            query: query
            size: 1000

    .then (body) ->
        State.set('celllines', body.hits.hits)

    .error (error) ->
        console.log error

State.select('filter').on('update', _.debounce(search, 200))


module.exports =
    search: search
