React = window.React

Elastic = require './elastic'

Table = require './components/table'
Search = require './components/search'

Elastic.search()

React.render <Search />, document.getElementById('search')
React.render <Table />, document.getElementById('table')
