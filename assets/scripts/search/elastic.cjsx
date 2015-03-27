_ = window._
Elasticsearch = window.elasticsearch

State = require './state'

elastic = Elasticsearch.Client
    hosts: 'localhost:9200'


buildFacetFilter = (facet) ->

    (item.name for item in facet.items when item.checked)


buildFacetFilters = () ->

    filters = _.object([facet.name, buildFacetFilter(facet)] for facet in State.select('filter', 'facets').get() when buildFacetFilter(facet).length > 0)

    if _.size(filters)
        terms: filters
    else
        null


buildQueryFilter = () ->

    query = State.select('filter', 'query').get()

    if query
        words = (w.toLowerCase() for w in query.split(/\s+/) when w != '')
        fields = State.select('query_fields').get()

        # for each word check all fields using (OR - match any field)
        parts = (({prefix: "#{field}": word} for field in fields) for word in words)
        ('or': (f for f in w) for w in parts)
    else
        null


buildQuery = () ->

    filters = (f for f in _.flatten([buildQueryFilter(), buildFacetFilters()]) when f)

    if filters.length
        constant_score:
            filter:
                and: filters
    else
        match_all: {}


search = () ->

    query = buildQuery()

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

State.select('filter').on('update', _.debounce(search, 100))


module.exports =
    search: search
