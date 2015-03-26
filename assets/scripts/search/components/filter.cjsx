React = window.React
State = require '../state'

Term = React.createClass

    render: () ->
        <li key={@props.index} onClick={@handleClick}>
            <div className="checkbox">{@props.item.name}</div>
            <label>{_.capitalize(@props.item.name)}</label>
            <div>{@props.item.checked and 'x' or 'o'}</div>
        </li>

    handleClick: (e) ->
        @props.cursor.set('checked', ! @props.cursor.get('checked'))

Facet = React.createClass

    render: () ->
        <ul>{(<Term index={index} item={item} cursor={@props.cursor.select('items').select(index)} /> for item, index in @props.facet.items)}</ul>

Facets = React.createClass

    mixins: [State.mixin]

    cursors:
        facets: ['filter', 'facets']

    render: () ->
        <ul>{(<Facet index={index} facet={facet} cursor={@cursors.facets.select(index)} /> for facet, index in @state.cursors.facets)}</ul>


module.exports = Facets
