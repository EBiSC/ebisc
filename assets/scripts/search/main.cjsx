React = window.React

Elastic = require './elastic'

Filter = require './components/filter'
Search = require './components/search'
Table = require './components/table'

Elastic.search()

React.render <Filter />, document.getElementById('filter')
React.render <Search />, document.getElementById('search')
React.render <Table />, document.getElementById('table')
