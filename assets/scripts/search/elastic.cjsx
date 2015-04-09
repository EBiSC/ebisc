XRegExp = require('xregexp').XRegExp
cookie = require('cookie-dough')()

State = require './state'
Config = require './config'

elastic = window.elasticsearch.Client
    host:
        protocol: window.location.protocol
        host: window.location.hostname
        port: window.location.port and window.location.port or window.location.protocol == 'https' and '443' or '80'
        path: '/es'
        headers: 'X-CSRFToken': cookie.get('csrftoken')

# -----------------------------------------------------------------------------
# Search

search = () ->

    body =
        size: 1000
        query: buildFilteredQuery()
        aggs: buildAggregations()

    orderBy = State.select('filter', 'orderBy').get()
    if orderBy != null
      body.sort = ["#{orderBy.field}": order: orderBy.direction]

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
        console.error JSON.stringify(error, null, '  ')
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
                min_doc_count: 0
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
