Config = require './config'
Elastic = require './elastic'
State = require './state'

Filter = require './components/filter'
Search = require './components/search'
Celllines = require './components/celllines'
TotalCount = require './components/total-count'

# Load session from sessionStorage or init from config

if sessionStorage.getItem('filter')
    State.set('filter', JSON.parse(sessionStorage.getItem('filter')))
else
    State.select('filter').set('facets', Config.facets)

onFilterUpdate = () ->
    sessionStorage.setItem('filter', JSON.stringify(State.select('filter').get()))
    Elastic.search()

State.select('filter').on('update', _.debounce(onFilterUpdate, 150))

React.render <TotalCount />, document.getElementById('total-count')
React.render <Filter />, document.getElementById('filter')
React.render <Search />, document.getElementById('search')
React.render <Celllines />, document.getElementById('celllines')
