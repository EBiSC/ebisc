State = require '../state'

Search = React.createClass

    mixins: [State.mixin]

    cursors:
        query: ['filter', 'query']

    getInitialState: () ->
        query: ''

    render: () ->
        <input type="text" placeholder="Search" value={@state.query} onChange={@handleChange} />

    handleChange: (e) ->
        @setState(query: e.target.value)
        @cursors.query.edit(e.target.value)

module.exports = Search
