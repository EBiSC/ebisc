Config = require './config'
Elastic = require './elastic'
State = require './state'

Filter = require './components/filter'
Search = require './components/search'
Table = require './components/table'

State.select('filter').set('facets', Config.facets)

State.select('filter').on('update', _.debounce(Elastic.search, 200))

React.render <Search />, document.getElementById('search')
React.render <Filter />, document.getElementById('filter')
React.render <Table cols={Config.fields} />, document.getElementById('table')
