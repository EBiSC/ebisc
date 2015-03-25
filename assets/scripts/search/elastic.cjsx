LoDash = require 'lodash'
Elasticsearch = require 'elasticsearch'

State = require './state'

elastic = new Elasticsearch.Client
    hosts: 'localhost:9200'

search = () ->

    query = State.select('query').get()

    if query
        body =
            query:
                prefix:
                    _all: query
    else
        body = 
            query:
                match_all: {}

    body.size = 1000

    elastic.search

            index: 'ebisc'
            type: 'cellline'
            body: body

        .then (body) ->
            State.set('celllines', body.hits.hits)

        .error (error) ->
            console.log error

State.select('query').on('update', LoDash.debounce(search, 100))

module.exports =
    search: search
