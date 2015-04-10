Elastic = require './elastic'
State = require './state'
Actions = require './actions'

Filter = require './components/filter'
Search = require './components/search'
Celllines = require './components/celllines'
TotalCount = require './components/total-count'

if sessionStorage.getItem('filter')
    # Load filter state from sessionStorage
    Actions.setFilter(JSON.parse(sessionStorage.getItem('filter')))
else
    # Init filter state from config
    Actions.initFilter()

onFilterUpdate = () ->
    sessionStorage.setItem('filter', JSON.stringify(State.select('filter').get()))
    Elastic.search()

State.select('filter').on('update', _.debounce(onFilterUpdate, 150))

React.render <TotalCount />, document.getElementById('total-count')
React.render <Filter />, document.getElementById('filter')
React.render <Search />, document.getElementById('search')
React.render <Celllines />, document.getElementById('celllines')
