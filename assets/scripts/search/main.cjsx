Config = require './config'
Elastic = require './elastic'
State = require './state'

Filter = require './components/filter'
Search = require './components/search'
Celllines = require './components/celllines'

State.select('filter').set('facets', Config.facets)

State.select('filter').on('update', _.debounce(Elastic.search, 100))

React.render <Search />, document.getElementById('search')

React.render <Filter />, document.getElementById('filter')

React.render <Celllines />, document.getElementById('celllines')
