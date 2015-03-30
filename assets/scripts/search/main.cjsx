Config = require './config'
Elastic = require './elastic'
State = require './state'

Filter = require './components/filter'
Search = require './components/search'
Celllines = require './components/celllines'
TotalCount = require './components/total-count'

State.select('filter').set('facets', Config.facets)

State.select('filter').on('update', _.debounce(Elastic.search, 150))

React.render <TotalCount />, document.getElementById('total-count')

React.render <Filter />, document.getElementById('filter')

React.render <Search />, document.getElementById('search')

React.render <Celllines />, document.getElementById('celllines')


