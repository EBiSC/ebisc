State = require './state'
Config = require './config'

initFilter = () ->
    State.select('filter').set('facets', Config.facets)

updateQueryFilter = (query) ->
    State.select('filter', 'query').edit(query)

updateFacetTermFilter = (facetName, term, state) ->
    selectedTerms = State.select('filter', 'facets', _.findIndex(State.select('filter', 'facets').get(), {name: facetName}), 'selectedTerms')
    selectedTerms.set(term, state)

orderBy = (value) ->
    State.select('filter').set('orderBy', value)

module.exports =
    initFilter: initFilter
    updateQueryFilter: updateQueryFilter
    updateFacetTermFilter: updateFacetTermFilter
    orderBy: orderBy
