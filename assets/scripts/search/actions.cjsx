State = require './state'

updateQueryFilter = (query) ->
    State.select('filter', 'query').edit(query)

updateFacetTermFilter = (facetName, term, state) ->
    selectedTerms = State.select('filter', 'facets', _.findIndex(State.select('filter', 'facets').get(), {name: facetName}), 'selectedTerms')
    selectedTerms.set(term, state)

module.exports =
    updateQueryFilter: updateQueryFilter
    updateFacetTermFilter: updateFacetTermFilter
