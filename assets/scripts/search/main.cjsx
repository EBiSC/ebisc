React = require 'react'

Elasticsearch = require 'elasticsearch'

State = require './state'
Table = require './components/table'
Search = require './components/search'

'SAMEA2590892'

elastic = new Elasticsearch.Client
    hosts: 'localhost:9200'

elastic.search

        index: 'ebisc'
        type: 'cellline'
        body:
            size: 1000
            query:
                match_all: {}

    .then (body) ->
        console.log "Found #{body.hits.total} celllines"
        console.log body
        State.set('celllines', body.hits.hits)

    .error (error) ->
        console.log error


React.render <Search />, document.getElementById('search')
React.render <Table />, document.getElementById('table')
