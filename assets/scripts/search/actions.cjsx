State = require './state'

setFilterFacetTerm = (facetName, term, state) ->
    selectedTerms = State.select('filter', 'facets', _.findIndex(State.select('filter', 'facets').get(), {name: facetName}), 'selectedTerms')
    selectedTerms.set(term, state)

module.exports =
    setFilterFacetTerm: setFilterFacetTerm
