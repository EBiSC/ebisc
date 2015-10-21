State = require './state'
Config = require './config'

initFilter = () ->
    State.select('filter').set('facets', Config.facets)

setFilter = (filter) ->
    State.set('filter', filter)

loadFilter = () ->
    setFilter(JSON.parse(sessionStorage.getItem('filter')))

saveFilter = () ->
    sessionStorage.setItem('filter', JSON.stringify(State.select('filter').get()))

updateQueryFilter = (query) ->
    State.select('filter', 'query').edit(query)

updateFacetTermFilter = (facetName, term, state) ->
    selectedTerms = State.select('filter', 'facets', _.findIndex(State.select('filter', 'facets').get(), {name: facetName}), 'selectedTerms')
    selectedTerms.set(term, state)

orderBy = (value) ->
    State.select('filter').set('orderBy', value)

module.exports =
    initFilter: initFilter
    setFilter: setFilter
    loadFilter: loadFilter
    saveFilter: saveFilter
    updateQueryFilter: updateQueryFilter
    updateFacetTermFilter: updateFacetTermFilter
    orderBy: orderBy
