State = require '../state'

Search = React.createClass

    mixins: [State.mixin]

    cursors:
        isLoaded: ['isLoaded']
        query: ['filter', 'query']

    getInitialState: () ->
        query: ''

    render: () ->
        <div>
        {
            if @state.cursors.isLoaded
                <input type="text" placeholder="Search" value={@state.query} onChange={@handleChange} />
        }
        </div>

    handleChange: (e) ->
        @setState(query: e.target.value)
        @cursors.query.edit(e.target.value)

module.exports = Search
