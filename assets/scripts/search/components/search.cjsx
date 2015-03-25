React = require 'react'
State = require '../state'

Search = React.createClass

    mixins: [State.mixin]

    cursors:
        celllines: ['celllines']

    render: () ->
        <input type="text" placeholder="Search" />

module.exports = Search
