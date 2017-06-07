XRegExp = require('xregexp').XRegExp

State = require './state'
Config = require './config'

elastic = window.elasticsearch.Client
    host:
        protocol: window.location.protocol
        host: window.location.hostname
        port: window.location.port and window.location.port or (window.location.protocol == 'https:' and 443 or 80)
        path: '/es'

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

    # console.log '-- QUERY BODY --'
    # console.log JSON.stringify(body, null, '  ')

    elastic.search
        index: 'ebisc'
        type: 'cellline'
        body: body

    .then (body) ->
        State.set('celllines', body.hits.hits)
        State.set('facetTerms', body.aggregations.facets) if body.aggregations
        State.set('isLoaded', true)

        # console.log '-- QUERY BODY --'
        # console.log JSON.stringify(body.aggregations.facets, null, '  ')

        changed = false
        facetFilter = State.select('filter', 'facets').get()

        for facet, i in facetFilter
            if body.aggregations.facets[facet.name].buckets
                matchingTerms = (bucket.key for bucket in body.aggregations.facets[facet.name].buckets)
            else
                matchingTerms = (bucket.key for bucket in body.aggregations.facets[facet.name].facet.buckets)
            for term, selected of facet.selectedTerms when selected and term not in matchingTerms
                changed = true
                facet.selectedTerms[term] = false

        if changed
            State.select('filter').set('facets', facetFilter)

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
    queryString = XRegExp.replace(queryString, XRegExp('[^(\\p{L}|\\d)]'), '')

    if not queryString
        return match_all: {}

    else

        multi_match:
            query: queryString
            type: 'best_fields'
            fields: Config.query_fields

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
        filters = buildFacetFilters()

        facets:
            global: {}
            aggs: _.object([facet.name, buildAggregation(facet, filters)] for facet in facets)


buildAggregation = (facet, filters) ->

    # If there are filters for other facets, use them to filter this facet (but do not use filter for this facet)
    otherFilters = (filter for filter in filters when not (facet.name of filter.terms))

    # If there is a query, use it to filter this facet
    query = buildQuery()
    if 'multi_match' of query
        otherFilters.push query: query

    terms =
        field: facet.name
        order: _term: 'asc'
        min_doc_count: 1
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


# -----------------------------------------------------------------------------

module.exports =
    search: search

# -----------------------------------------------------------------------------
