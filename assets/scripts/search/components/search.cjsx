State = require '../state'
Actions = require '../actions'

Search = React.createClass

    mixins: [State.mixin]

    cursors:
        isLoaded: ['isLoaded']
        query: ['filter', 'query']

    render: () ->
        <div>
        {
            if @state.cursors.isLoaded
                <Input query={@state.cursors.query} />
        }
        </div>

Input = React.createClass

    getInitialState: () ->
        query: @props.query

    render: () ->
        <input type="text" placeholder="Enter keywords" value={@state.query} onChange={@handleChange} />

    handleChange: (e) ->
        @setState(query: e.target.value)
        Actions.updateQueryFilter(e.target.value)

module.exports = Search
